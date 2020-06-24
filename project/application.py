from passlib.apps import custom_app_context as pwd_context
from tkinter import *
import tkinter.filedialog
import time

from tkinter import messagebox as pop_up

EMPTY_TITLE_ERROR_MESSAGE_OPEN = "Please write the name of the file you want to open in the given field."
FILE_NOT_FOUND_ERROR_MESSAGE = "No file with the given title was found, remember that this text editor can only read files in its directory."

root = tkinter.Tk()
text=Text(root)
text.grid()

scrollb = Scrollbar(root, command=text.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
text['yscrollcommand'] = scrollb.set

def help():
    root = tkinter.Tk()
    texta=Text(root)
    texta.grid()
    texta.insert(END,"""HELP\n\nThis is a bare-bones text-editor made in Python and the tkinter framework.
Type in the textbox. To save your text, click on Options and choose Save.
To open a file(In the same directory as this program), enter the filename in the entry box above the Options button.
Then click Options and choose Open.
To add the Date, click Options and choose Date.
To convert the text to leetspeak, click Options and choose Convert to LeetSpeak.
To hash the text, click Options and choose Hash.
To check the text for spelling mistakes, click Options and choose Check for Mistakes.
To change the font color, click Color and choose.
To change the the font, click Font and choose.""")


def saveas():                                                   #  Function to save file
    global text
    t = text.get("1.0", "end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def leet():                                                     # Function to convert text to 1337speak
    t = text.get("1.0", "end-1c")
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"@","e":"3","i":"1","l":"1","o":"0","s":"5","t":"7"}
    data = ''.join(getchar(c) for c in t)
    text.delete("1.0", "end")
    text.insert(END,data)
    text.after(1000, leet)

def hash():                                                     # Function to hash text
    t = text.get("1.0", "end-1c")
    data = pwd_context.hash(t)
    text.delete("1.0", "end")
    text.insert(END,data)
    text.after(1000, hash)

def check():
    root = tkinter.Tk()
    text2=Text(root)
    text2.grid()
    text2.insert(END,"MISSPELLED WORDS:\n")
    global text
    t = text.get("1.0", "end-1c")
    words = open("dictionary.txt").readlines()
    words = [word.strip() for word in words]
    hash = {}
    for word in words:
        hash[word] = True
    for word in t.split():
        found = word in hash
        if found == False:
            if word.isalpha():
                text2.insert(END,word + "\n")



#Functions for fonts
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

def FontMonaco():
    global text
    text.config(font="Monaco")

def FontArial():
    global text
    text.config(font="Arial")

def FontFutura():
    global text
    text.config(font="Futura")

def FontNote():
    global text
    text.config(font="Noteworthy")

def FontCalibri():
    global text
    text.config(font="Calibri")

#Functions for colors
def ColorRed():
    global text
    text.config(fg="Red")

def ColorBlue():
    global text
    text.config(fg="Blue")

def ColorGreen():
    global text
    text.config(fg="Green")

def ColorBrown():
    global text
    text.config(fg="Brown")

def ColorYellow():
    global text
    text.config(fg="Yellow")

def ColorOrange():
    global text
    text.config(fg="Orange")

def ColorPurple():
    global text
    text.config(fg="Purple")


def add_date():
    full_date = time.localtime()
    day = str(full_date.tm_mday)
    month = str(full_date.tm_mon)
    year = str(full_date.tm_year)
    date = ("\n"+day+'/'+month+'/'+year)
    text.insert(tkinter.INSERT, date, "a")

def _open():
    if not file_title.get():
        pop_up.showerror("Title is empty.",EMPTY_TITLE_ERROR_MESSAGE_OPEN)
        return 1
    filename = file_title.get()
##    if not ".txt" in file_title.get():
##        filename = file_title.get() + ".txt"

    try:
        with open(filename) as f:
            text.delete("1.0",tkinter.END)
            text.insert(tkinter.INSERT, f.read(), "a")
    except IOError:
        pop_up.showerror("File not found.",FILE_NOT_FOUND_ERROR_MESSAGE)


##EMPTY_TITLE_ERROR_MESSAGE_OPEN = "Please write the name of the file you want to open in the given field."


top = tkinter.Frame(root)
temp = tkinter.Label(root,text="Title:")
temp.pack(in_ = top,side=tkinter.LEFT)

file_title = tkinter.Entry(root)
file_title.pack(in_ = top,side=tkinter.RIGHT)
file_title.insert(0, 'File to open')
file_title.bind("<FocusIn>", lambda args: file_title.delete('0', 'end'))
file_title.grid()

opt=Menubutton(root, text="Options")
opt.grid()
opt.menu=Menu(opt, tearoff=0)
opt["menu"]=opt.menu
opt.menu.add_command(label="Open", command=_open)
opt.menu.add_command(label="Save", command=saveas)
opt.menu.add_command(label="Add date",command=add_date)
opt.menu.add_command(label="Convert to LeetSpeak",command=leet)
opt.menu.add_command(label="Hash",command=hash)
opt.menu.add_command(label="Check for Mistakes",command=check)
opt.menu.add_command(label="Help",command=help)

color=Menubutton(root, text="Colour")
color.grid()
color.menu=Menu(color, tearoff=0)
color["menu"]=color.menu

font=Menubutton(root, text="Font")
font.grid()
font.menu=Menu(font, tearoff=0)
font["menu"]=font.menu


Helvetica=IntVar()
Monaco=IntVar()
Arial=IntVar()
Courier=IntVar()
Futura=IntVar()
Note=IntVar()
Felt=IntVar()

Red=IntVar()
Blue=IntVar()
Green=IntVar()
Brown=IntVar()
Yellow=IntVar()
Orange=IntVar()
Purple=IntVar()


font.menu.add_checkbutton(label="Courier", variable=Courier,
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
command=FontHelvetica)
font.menu.add_checkbutton(label="Monaco", variable=Monaco,
command=FontMonaco)
font.menu.add_checkbutton(label="Arial", variable=Arial,
command=FontArial)
font.menu.add_checkbutton(label="Futura", variable=Futura,
command=FontFutura)
font.menu.add_checkbutton(label="Noteworthy", variable=Note,
command=FontNote)
font.menu.add_checkbutton(label="Calibri", variable=Felt,
command=FontCalibri)

color.menu.add_checkbutton(label="Red", variable=Red,
command=ColorRed)
color.menu.add_checkbutton(label="Blue", variable=Blue,
command=ColorBlue)
color.menu.add_checkbutton(label="Green", variable=Green,
command=ColorGreen)
color.menu.add_checkbutton(label="Brown", variable=Brown,
command=ColorBrown)
color.menu.add_checkbutton(label="Yellow", variable=Yellow,
command=ColorYellow)
color.menu.add_checkbutton(label="Orange", variable=Orange,
command=ColorOrange)
color.menu.add_checkbutton(label="Purple", variable=Purple,
command=ColorPurple)


root.mainloop()
