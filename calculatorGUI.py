from tkinter import *

root = Tk()

i = 0
operand = ''
x = ''

def insert(text):
    global i
    screen.insert(i,text)
    i += 1

def operate(operator):
    global operand
    global x
    operand = operator
    x = screen.get()
    screen.delete(0,END)

def execute():
    global operand
    global x
    
    if operand in '+-/x':
        if operand == '+':
            result = float(x) + float(screen.get())
        elif operand == '-':
            result = float(x) - float(screen.get())
        elif operand == '/':
            result = float(x)/float(screen.get())
        else:
            result = float(x)* float(screen.get())

    screen.delete(0,END)
    screen.insert(0, str(result))

num1 = Button(root,text = "1",command = lambda:insert("1"))
num2 = Button(root,text = "2",command = lambda:insert("2"))
num3 = Button(root,text = "3",command = lambda:insert("3"))
num4 = Button(root,text = "4",command = lambda:insert("4"))
num5 = Button(root,text = "5",command = lambda:insert("5"))
num6 = Button(root,text = "6",command = lambda:insert("6"))
num7 = Button(root,text = "7",command = lambda:insert("7"))
num8 = Button(root,text = "8",command = lambda:insert("8"))
num9 = Button(root,text = "9",command = lambda:insert("9"))
dot = Button(root, text = ".",command = lambda:insert("."))
num0 = Button(root,text = "0",command = lambda:insert("0"))

plus = Button(root, text = '+',command = lambda:operate("+"))
plus.grid(row = 1, column = 3, ipadx = 10)
minus = Button(root, text = '-',command = lambda:operate("-"))
minus.grid(row = 2, column = 3, ipadx = 10)
multi = Button(root, text = 'x',command = lambda:operate("x"))
multi.grid(row = 3, column = 3, ipadx = 10)
divide = Button(root, text = '/',command = lambda:operate("/"))
divide.grid(row = 4, column = 3, ipadx = 10)

sum = Button(root, text = "=",command = lambda:execute())
sum.grid(row = 4, column = 2, ipadx = 10)

screen = Entry(root)
screen.grid(row = 0, columnspan = 3)

clear = Button(root,text = "CLEAR",command = lambda:screen.delete(0,END))
clear.grid(row = 0,column = 3,ipadx = 0)

num1.grid(row = 1, column = 0,ipadx = 10)
num2.grid(row = 1, column = 1,ipadx = 10)
num3.grid(row = 1, column = 2,ipadx = 10)
num4.grid(row = 2, column = 0,ipadx = 10)
num5.grid(row = 2, column = 1,ipadx = 10)
num6.grid(row = 2, column = 2,ipadx = 10)
num7.grid(row = 3, column = 0,ipadx = 10)
num8.grid(row = 3, column = 1,ipadx = 10)
num9.grid(row = 3, column = 2,ipadx = 10)
dot.grid(row = 4, column = 0, ipadx = 10)
num0.grid(row = 4, column = 1,ipadx = 10)

root.mainloop()