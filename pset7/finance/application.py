from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import re
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

    data = db.execute("""SELECT * FROM record WHERE id = :id""", id=session["user_id"])
    grand_tot = 0
    cash_info = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    for row in data:
        symbol = row["stock"]
        shares = row["amount"]
        stock = lookup(symbol)
        total = shares * float(stock["price"])
        grand_tot += total
        db.execute("UPDATE record SET price=:price, \
                    value=:total WHERE id=:id AND stock=:symbol", \
                    price=usd(stock["price"]), \
                    total=usd(total), id=session["user_id"], symbol=symbol)
    grand_tot += cash_info[0]["cash"]
    new_data = db.execute("SELECT * from record \
                                    WHERE id=:id", id=session["user_id"])
    return render_template("index.html", stocks=new_data, cash = usd(cash_info[0]["cash"]), total = usd(grand_tot))


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



        # Table which records all transactions ever made

        db.execute("""INSERT INTO trans (id, stock, shares, total, type)
                      VALUES (:id, :stock, :shares, :total, :type)""",
                    id=session.get("user_id"),
                    stock=request.form.get("symbol"),
                    shares=shares,
                    total = symb["price"] * shares,
                    type="buy")

        previous_shares = db.execute("""SELECT amount FROM record WHERE stock = :stock AND id = :id""", stock=request.form.get("symbol"), id=session["user_id"])
        previous_value = db.execute("""SELECT value FROM record WHERE stock = :stock AND id = :id""", stock=request.form.get("symbol"), id=session["user_id"])

        if not previous_shares:
            db.execute("""INSERT INTO record (id, stock, amount, price, value)
                          VALUES (:id, :stock, :amount, :price, :value)""",
                        id=session.get("user_id"),
                        stock=request.form.get("symbol"),
                        amount=shares,
                        price=symb["price"],
                        value = symb["price"] * shares)
        else:
            new_amount = int(previous_shares[0]["amount"]) + shares
            new_value = int(previous_value[0]["value"] + symb["price"]) * shares

            db.execute("""UPDATE record SET amount = :amount WHERE id = :id AND stock = :stock""", amount = new_amount, id=session["user_id"], stock=request.form.get("symbol"))
            db.execute("""UPDATE record SET value = :value WHERE id = :id AND stock = :stock""", value = new_value, id=session["user_id"], stock=request.form.get("symbol"))

        return redirect(url_for("index"))

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    histories = db.execute("SELECT * from trans WHERE id=:id", id=session["user_id"])

    return render_template("history.html", trans=histories)

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
        return render_template("quoted.html", stock=usd(symbol))

    elif request.method == "GET":
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        if not request.form.get("username") or not request.form.get("password") or request.form.get("password") != request.form.get("confirmation"):
            return apology("retry", 400)

        # insert the new user into users, storing the hash of the user's password
        result = db.execute("INSERT INTO users (username, hash, cash) \
                             VALUES(:username, :hash, :cash)", \
                             username=request.form.get("username"), \
                             hash=pwd_context.hash(request.form.get("password")), \
                             cash=10000)

        if not result:
            return apology("Username already exist")

        # remember which user has logged in
        session["user_id"] = result

        # redirect user to home page
        return redirect(url_for("index"))

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
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


        name_of_us = db.execute("""SELECT * FROM users WHERE id = :id""", id=session["user_id"])

        name = name_of_us[0]["username"]

        db.execute("UPDATE users SET cash = cash + :purchase WHERE id = :id", id=session["user_id"], purchase=symb["price"] * float(shares))

        new_cash = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])

        foo = new_cash[0]["cash"]



        # Table which records all transactions ever made

        db.execute("""INSERT INTO trans (id, stock, shares, total, type)
                      VALUES (:id, :stock, :shares, :total, :type)""",
                    id=session.get("user_id"),
                    stock=request.form.get("symbol"),
                    shares=shares,
                    total = symb["price"] * shares,
                    type="sell")

        previous_shares = db.execute("""SELECT amount FROM record WHERE stock = :stock AND id = :id""", stock=request.form.get("symbol"), id=session["user_id"])
        previous_value = db.execute("""SELECT value FROM record WHERE stock = :stock AND id = :id""", stock=request.form.get("symbol"), id=session["user_id"])

        if not previous_shares:
            # db.execute("""INSERT INTO record (id, stock, amount, price, value)
            #               VALUES (:id, :stock, :amount, :price, :value)""",
            #             id=session.get("user_id"),
            #             stock=request.form.get("symbol"),
            #             amount=shares,
            #             price=symb["price"],
            #             value = symb["price"] * shares)
            return apology("Can't sell something you don't have", 400)

        else:
            new_amount = int(previous_shares[0]["amount"]) - shares
            new_value = float(float(previous_value[0]["value"][1:]) - symb["price"]) * shares

            db.execute("""UPDATE record SET amount = :amount WHERE id = :id AND stock = :stock""", amount = new_amount, id=session["user_id"], stock=request.form.get("symbol"))
            db.execute("""UPDATE record SET value = :value WHERE id = :id AND stock = :stock""", value = new_value, id=session["user_id"], stock=request.form.get("symbol"))

        return redirect(url_for("index"))

    else:
        return render_template("sell.html")