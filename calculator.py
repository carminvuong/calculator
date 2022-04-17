from tkinter import *


root = Tk()
root.title("Calculator")

# setting the favicon
image = PhotoImage(file="logo.png")
root.iconphoto(False, image)


# add entry box to window
entry = Entry(root, width=60, bd=4)
entry.grid(row=0, column=0, columnspan = 4)

# button functions
def buttonClick(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def turnPercentage():
    currentNumber = float(entry.get())
    entry.delete(0, END)
    entry.insert(0, str(currentNumber/100))

def negate():
    currentNumber = int(entry.get())
    entry.delete(0, END)
    entry.insert(0, str(currentNumber * -1))



# make all the buttons
button1 = Button(root, text="1", height=5, width=12, command=lambda: buttonClick(1))
button2 = Button(root, text="2", height=5, width=12, command=lambda: buttonClick(2))
button3 = Button(root, text="3", height=5, width=12, command=lambda: buttonClick(3))
button4 = Button(root, text="4", height=5, width=12, command=lambda: buttonClick(4))
button5 = Button(root, text="5", height=5, width=12, command=lambda: buttonClick(5))
button6 = Button(root, text="6", height=5, width=12, command=lambda: buttonClick(6))
button7 = Button(root, text="7", height=5, width=12, command=lambda: buttonClick(7))
button8 = Button(root, text="8", height=5, width=12, command=lambda: buttonClick(8))
button9 = Button(root, text="9", height=5, width=12, command=lambda: buttonClick(9))
button0 = Button(root, text="0", height=5, width=12*2+2, command=lambda: buttonClick(0))

buttonPlus = Button(root, text="+", height=5, width=12, command=buttonClick)
buttonMinus = Button(root, text="-", height=5, width=12, command=buttonClick)
buttonDivide = Button(root, text="÷", height=5, width=12, command=buttonClick)
buttonMultiply = Button(root, text="*", height=5, width=12, command=buttonClick)
buttonEquals = Button(root, text="=", height=5, width=12*2+2, command=buttonClick)
buttonNegate = Button(root, text="-/+", height=5, width=12, command=negate)
buttonClearScreen = Button(root, text="CLEAR", height=5, width=12, command=buttonClick)
buttonPercent = Button(root, text="%", height=5, width=12, command=turnPercentage)
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
buttonEquals.grid(row=5, column=2, columnspan=2)

# running the program
root.mainloop()