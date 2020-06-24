from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    return apology("TODO")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Enter a symbol.")
        symb = lookup(request.form.get("symbol"))

        if not symb:
            return apology("Invalid symbol. Re-enter.")

        try:
            shares = int(request.form.get("shares"))
            if shares < 0:
                return apology("Shares must be positive integer")
        except:
            return apology("Shares must be positive integer")


        cash_info = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        if float(cash_info[0]["cash"]) < symb["price"] * shares:
            return apology("Not enough funds.")

        name_of_us = db.execute("""SELECT * FROM users WHERE id = :id""", id=session["user_id"])

        name = name_of_us[0]["username"]

        db.execute("UPDATE users SET cash = cash - :purchase WHERE id = :id", id=session["user_id"], purchase=symb["price"] * float(shares))

        new_cash = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])

        foo = new_cash[0]["cash"]

        db.execute("""UPDATE {} SET cash = ''""".format(name))                                                          # Previously, multiple cash entries would appear

        db.execute("""DELETE FROM {} WHERE stock IS NULL""".format(name))                                               # Delete any empty rows

        db.execute("""UPDATE {}_index SET cash = ''""".format(name))                                                    # (user_index)Previously, multiple cash entries would appear

        db.execute("""DELETE FROM {}_index WHERE stock IS NULL""".format(name))                                         # (user_index)Delete any empty rows

        db.execute("""INSERT INTO {} (stock, amount, price, tot_value, cash)
                      VALUES (:stock, :amount, :price, :tot_value, :cash_f)""".format(name),
                    stock=request.form.get("symbol"),
                    amount=request.form.get("shares"),
                    price=symb["price"] * shares,
                    tot_value = symb["price"] * shares,
                    cash_f = foo)

        # Table which records all transactions ever made

        db.execute("""INSERT INTO trans (id, stock, shares, total, type)
                      VALUES (:id, :stock, :shares, :total, :type)""",
                    id=session.get("user_id"),
                    stock=request.form.get("symbol"),
                    shares=shares,
                    total = symb["price"] * shares,
                    type="buy")



        # Creates a temporary table spare which stores all the data needed for index()

        db.execute("""CREATE TABLE spare (id INTEGER, stock TEXT, shares INTEGER, total INTEGER)""")

        amounts_to_be_changed = db.execute("""SELECT shares, total FROM {}_index WHERE stock=:stock""".format(name), symbol)

        new_shares = int(amounts_to_be_changed[0]['shares']) + amount

        new_total = int(amounts_to_be_changed[0]['total']) + value

        bar = db.execute("""INSERT INTO spare (id, stock) SELECT id, stock FROM trans GROUP BY id, stock""")

        db.execute("""INSERT INTO spare (shares, total) WHERE stock=:stock VALUES (:shares, :total)""", stock=symbol, shares=new_shares, total=new_total)

        # Inserts the data for index() into spare
        ###### Ran into a problem here: bar previously worked for buy, but now we need to keep track of the amount of each stock, not the sum for history
        ###### Solution: if a stocks type is sell: SUM it. If buy: SUM it
        ###### Then subtract sell from buy

        bar = db.execute("""INSERT INTO spare (id, stock, shares, total) SELECT id, stock, SUM(shares), SUM(total) FROM trans GROUP BY id, stock""")

        # db.execute("""INSERT INTO spare (id, stock, shares, total)
        #               VALUES (:id :stock, :shares, :total")""",
        #               id=session["user_id"],
        #               stock=bar[0]['stock'],
        #               shares=bar[0]['SUM(shares)'],
        #               total=bar[0]['SUM(total)'])

        # Takes all the data relevant to the current user for index() and stores it in that users table

        db.execute("""INSERT INTO {}_index (stock, amount, tot_value)
                    SELECT stock, shares, total FROM spare WHERE id=:id;""".format(name), id=session.get("user_id"))

        # Fill other two fields: price and cash

        db.execute("""INSERT INTO {}_index (cash)
                    VALUES (:cash)""".format(name),
                    cash=foo)

        # baz = db.execute("""SELECT * FROM {}_index""".format(name))
        # for idx, row in enumerate(baz):
        #     price_index = baz[idx][float('tot_value')] / baz[idx][float('amount')]

        #     db.execute("""INSERT INTO {}_index (price)
        #                 VALUES (:price)""".format(name),
        #                 price=price_index)


        db.execute("""DROP TABLE spare;""")

        return redirect(url_for("index"))

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    histories = db.execute("SELECT * from trans WHERE id=:id", id=session["user_id"])

    return render_template("history.html", histories=histories)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))
        if not symbol:
            return apology("Invalid symbol. Please re-enter.")
        return render_template("quoted.html", stock=symbol)

    elif request.method == "GET":
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    # if request.method == "POST":

    #     # ensure username was submitted
    #     if not request.form.get("username"):
    #         return apology("Must provide username")

    #     # ensure password was submitted
    #     elif not request.form.get("password"):
    #         return apology("Must provide password")

    #     # # ensure password and verified password is the same
    #     # elif request.form.get("password") != request.form.get("passwordagain"):
    #     #     return apology("password doesn't match")

    #     # insert the new user into users, storing the hash of the user's password
    #     result = db.execute("INSERT INTO users (username, hash) \
    #                          VALUES(:username, :hash)", \
    #                          username=request.form.get("username"), \
    #                          hash=pwd_context.hash(request.form.get("password")))
    #     user_table = db.execute("CREATE TABLE {} ('stock' TEXT, 'amount' INTEGER, 'price' INTEGER, 'tot_value' INTEGER, 'type' TEXT, 'cash' INTEGER)".format(request.form.get("username")))


    #     # Table # 2 for index()
    #     user_table_index = db.execute("CREATE TABLE {}_index ('stock' TEXT, 'amount' INTEGER, 'price' INTEGER, 'tot_value' INTEGER, 'cash' INTEGER)".format(request.form.get("username")))

    #     if not result:
    #         return apology("Username already exists")

    #     # remember which user has logged in
    #     session["user_id"] = result

    #     return redirect(url_for("index"))

    # else:
    #     return render_template("register.html")
    """Register user."""

    # if user reached route via GET, return register page
    if request.method == "GET":
        return render_template("register.html")

    # otherwise, if reached via POST i.e. submitting a form...
    elif request.method == "POST":
        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # ensure password and confirmation are equal
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password fields do not match")

        # encrypt password
        hash = pwd_context.encrypt(request.form.get("password"))

        # comment
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"),hash=hash)
        if not result:
            return apology("username already in use")

        user_table = db.execute("CREATE TABLE {} ('stock' TEXT, 'amount' INTEGER, 'price' INTEGER, 'tot_value' INTEGER, 'type' TEXT, 'cash' INTEGER)".format(request.form.get("username")))



        # Table # 2 for index()
         user_table_index = db.execute("CREATE TABLE {}_index ('stock' TEXT, 'amount' INTEGER, 'price' INTEGER, 'tot_value' INTEGER, 'cash' INTEGER)".format(request.form.get("username")))

        # log user in
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        flash('Successfully registered!')
        return redirect(url_for("index"))

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    if request.method == "POST":

        user_info = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])

        name = user_info[0]["username"]
        cash = user_info[0]["cash"]
        foo = user_info[0]["cash"]

        if not request.form.get("symbol"):
            return apology("Enter a symbol.")
        symbol = lookup(request.form.get("symbol"))
        symb = request.form.get("symbol")

        if not symbol:
            return apology("Invalid symbol. Re-enter.")

        try:
            shares = int(request.form.get("shares"))
            if shares < 0:
                return apology("Shares must be positive integer")
        except:
            return apology("Shares must be positive integer")
        value = symbol["price"] * shares


        db.execute("UPDATE users SET cash = cash + :sold WHERE id = :id", id=session["user_id"], sold=value)

        # Table which records all transactions ever made

        db.execute("""INSERT INTO trans (id, stock, shares, total, type)
                      VALUES (:id, :stock, :shares, :total, :type)""",
                    id=session.get("user_id"),
                    stock=request.form.get("symbol"),
                    shares=shares,
                    total = symbol["price"] * shares,
                    type="sell")

        # Creates a temporary table spare which stores all the data needed for index()

        db.execute("""CREATE TABLE spare (id INTEGER, stock TEXT, shares INTEGER, total INTEGER)""")

        # Inserts the data for index() into spare

        # amounts_to_be_changed = db.execute("""SELECT amount, tot_value FROM {}_index WHERE stock=:stock""".format(name), stock=symb)

        # new_shares = int(amounts_to_be_changed[0]['amount']) - amount

        # new_total = int(amounts_to_be_changed[0]['tot_value']) - value

        # bar = db.execute("""INSERT INTO spare (id, stock) SELECT id, stock FROM trans GROUP BY id, stock""")

        # db.execute("""INSERT INTO spare (shares, total) WHERE stock=:stock VALUES (:shares, :total)""", stock=symb, shares=new_shares, total=new_total)

        # baz = db.execute("""SELECT * FROM trans GROUP BY id, stock, type""")

        # # db.execute("""INSERT INTO spare (id, stock, shares, total)
        # #               VALUES (:id :stock, :shares, :total")""",
        # #               id=session["user_id"],
        # #               stock=bar[0]['stock'],
        # #               shares=bar[0]['SUM(shares)'],
        # #               total=bar[0]['SUM(total)'])

        # # Takes all the data relevant to the current user for index() and stores it in that users table

        # db.execute("""INSERT INTO {}_index (stock, amount, tot_value)
        #             SELECT stock, shares, total FROM spare WHERE id=:id;""".format(name), id=session.get("user_id"))

        # # Fill other two fields: price and cash

        # db.execute("""INSERT INTO {}_index (cash)
        #             VALUES (:cash)""".format(name),
        #             cash=foo)

        # baz = db.execute("""SELECT * FROM {}_index""".format(name))
        # for idx, row in enumerate(baz):
        #     price_index = baz[idx][float('tot_value')] / baz[idx][float('amount')]

        #     db.execute("""INSERT INTO {}_index (price)
        #                 VALUES (:price)""".format(name),
        #                 price=price_index)


        db.execute("""DROP TABLE spare;""")

        return redirect(url_for("index"))

    else:
        return render_template("sell.html")
