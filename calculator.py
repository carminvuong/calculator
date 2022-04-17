from tkinter import *


root = Tk()
root.title("Calculator")
root.resizable(False, False)

# setting the favicon
image = PhotoImage(file="logo.png")
root.iconphoto(False, image)


# add entry box to window
entry = Entry(root, width=60, bd=4, justify="right")
entry.grid(row=0, column=0, columnspan = 4)

# button functions

# global variables
operation = ""
firstNumber = 0



def resetOperationColors():
    buttonPlus.configure(bg="#FFA93C", fg="white")
    buttonMinus.configure(bg="#FFA93C", fg="white")
    buttonDivide.configure(bg="#FFA93C", fg="white")
    buttonMultiply.configure(bg="#FFA93C", fg="white")


def buttonClick(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))
    resetOperationColors()


def turnPercentage():
    currentNumber = float(entry.get())
    entry.delete(0, END)
    entry.insert(0, str(currentNumber/100))

def negate():
    currentNumber = float(entry.get())
    entry.delete(0, END)
    entry.insert(0, str(currentNumber * -1))

def add():
    global firstNumber
    firstNumber = float(entry.get())
    global operation
    operation = "+"
    entry.delete(0, END)
    buttonPlus.configure(bg="white", fg="#FFA93C")

def subtract():
    global firstNumber
    firstNumber = float(entry.get())
    global operation
    operation = "-"
    entry.delete(0, END)
    buttonMinus.configure(bg="white", fg="#FFA93C")


def multiply():
    global firstNumber
    firstNumber = float(entry.get())
    global operation
    operation = "*"
    entry.delete(0, END)
    buttonMultiply.configure(bg="white", fg="#FFA93C")

def divide():
    global firstNumber
    firstNumber = float(entry.get())
    global operation
    operation = "/"
    entry.delete(0, END)
    buttonDivide.configure(bg="white", fg="#FFA93C")
    

def equals():
    secondNumber = float(entry.get())
    entry.delete(0, END)
    if operation == "+":
        entry.insert(0, str(firstNumber + secondNumber))
    elif operation == "*":
        entry.insert(0, str(firstNumber * secondNumber))
    elif operation == "-":
        entry.insert(0, str(firstNumber - secondNumber))
    elif operation == "/":
        entry.insert(0, str(firstNumber / secondNumber))

def clear():
    entry.delete(0, END)
    resetOperationColors()

def addDecimalPoint():
    current = entry.get()
    entry.delete(0, END)
    if current == "":
        entry.insert(0, "0.")
    else:
        entry.insert(0, current + ".")







# make all the buttons
button1 = Button(root, bg="#8F8F8F", fg="white", text="1", height=5, width=12, command=lambda: buttonClick(1))
button2 = Button(root, bg="#8F8F8F", fg="white", text="2", height=5, width=12, command=lambda: buttonClick(2))
button3 = Button(root, bg="#8F8F8F", fg="white", text="3", height=5, width=12, command=lambda: buttonClick(3))
button4 = Button(root, bg="#8F8F8F", fg="white", text="4", height=5, width=12, command=lambda: buttonClick(4))
button5 = Button(root, bg="#8F8F8F", fg="white", text="5", height=5, width=12, command=lambda: buttonClick(5))
button6 = Button(root, bg="#8F8F8F", fg="white", text="6", height=5, width=12, command=lambda: buttonClick(6))
button7 = Button(root, bg="#8F8F8F", fg="white", text="7", height=5, width=12, command=lambda: buttonClick(7))
button8 = Button(root, bg="#8F8F8F", fg="white", text="8", height=5, width=12, command=lambda: buttonClick(8))
button9 = Button(root, bg="#8F8F8F", fg="white", text="9", height=5, width=12, command=lambda: buttonClick(9))
button0 = Button(root, bg="#8F8F8F", fg="white", text="0", height=5, width=12*2+2, command=lambda: buttonClick(0))

buttonPlus = Button(root, bg="#FFA93C", fg="white", text="+", height=5, width=12, command=add)
buttonMinus = Button(root, bg="#FFA93C", fg="white", text="-", height=5, width=12, command=subtract)
buttonDivide = Button(root, bg="#FFA93C", fg="white", text="÷", height=5, width=12, command=divide)
buttonMultiply = Button(root, bg="#FFA93C", fg="white", text="*", height=5, width=12, command=multiply)
buttonEquals = Button(root, bg="#FFA93C", fg="white", text="=", height=5, width=12, command=equals)
buttonNegate = Button(root, bg="#C6C6C6", fg="black", text="-/+", height=5, width=12, command=negate)
buttonClearScreen = Button(root, bg="#C6C6C6", fg="black", text="CLEAR", height=5, width=12, command=clear)
buttonPercent = Button(root, bg="#C6C6C6", fg="black", text="%", height=5, width=12, command=turnPercentage)
buttonDecimalPoint = Button(root, bg="#8F8F8F", fg="white", text=".", height=5, width=12, command=addDecimalPoint)
# consider adding decimal point Button


# positioning the buttons on the window screen
buttonClearScreen.grid(row=1, column=0)
buttonNegate.grid(row=1, column=1)
buttonPercent.grid(row=1, column=2)
buttonDivide.grid(row=1, column=3)


button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonMultiply.grid(row=2, column=3)


button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonMinus.grid(row=3, column=3)


button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
buttonPlus.grid(row=4, column=3)

button0.grid(row=5, column=0, columnspan=2)
buttonDecimalPoint.grid(row=5, column=2)
buttonEquals.grid(row=5, column=3)


# running the program
root.mainloop()