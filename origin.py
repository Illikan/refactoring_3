#!/usr/bin/python

# Shino's Reverse Polish Notation calculator with basic functionality.
# Going to add some new operations in the near future.

from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.
rt = Tk() # The root.
rt.title("RPN Calc 1.1 by Shino") # The title of the application.
rt.resizable(0, 0) # The window should not be resizable.
mf = ttk.Frame(rt)
argument, stacklist = StringVar(), StringVar() # For changing the content of the certain elements of the application.
mf.grid(column = 0, row = 0, sticky = (N, W, E, S)) # Everything is displayed in a grid.
label0 = Label(mf, textvariable = stacklist)
label0.grid(row = 0, columnspan = 3)
label1 = Label(mf, textvariable = argument, background = "white")
label1.grid(row = 0, column = 3)
stack, num = [], ''

    
def construct_number(symbol:int):
    global num, argument
    symbol = str(symbol)
    if num == '0' and symbol == '0':
        tkinter.messagebox.showinfo("The error", "Can't begin with a zero.") 
    else:
        num += symbol
        argument.set(num)

def construct_dot(): # The dot.
    global num, argument
    if '.' in num:
        tkinter.messagebox.showinfo("The error", "A dot is used already.")
    elif num == '':
        num += "0."
        argument.set(num)
    else:
        num += '.'
        argument.set(num)
def construct_minus(): # The minus.
    global num, argument
    if num == '':
        num += '-'
        argument.set(num)
    else:
        tkinter.messagebox.showinfo("The error", "A minus can be put only in the beginning.")
        
def goback(): # The "backspace".
    global num, argument
    if num == '':
        tkinter.messagebox.showinfo("The error", "It's empty already.")
    else:
        num = num[:-1]
        argument.set(num)
def delfromstack(): # Deleting elements from the stack.
    global stacklist, stack
    if len(stack) == 0:
        tkinter.messagebox.showinfo("The error", "There is nothing on the stack.")
    else:
        stack = stack[:-1]
        if len(stack) == 0:
            stacklist.set('')
        else:
            stacklist.set(', '.join([str(x) for x in stack]))

def push(): # Pushing on the stack.
    global num, stacklist, argument
    if float(num) % 1 == 0.0:
        stack.append(int(num))
    else:
        stack.append(float(num))
    stacklist.set(', '.join([str(x) for x in stack]))
    argument.set('')
    num = ''


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
def perform_operation(symbol:str):
    global stack
    if len(stack) < 2:
        tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
    else:
        match symbol:
            case '+':
                stack[-2] = stack[-2] + stack[-1]
            case '-':
                stack[-2] = stack[-2] - stack[-1]
            case '*':
                stack[-2] = stack[-2] * stack[-1]
            case '/':
                if stack[-1] == 0:
                    tkinter.messagebox.showinfo("The error", "The divisior is 0, can't perform the division.")
                else:
                    stack[-2] = int((stack[-2] / stack[-1]) * 1000000 + 0.5) / 1000000.0
        # stack[-2] = stack[-2] + stack[-1]
        del stack[-1]
        if stack[-1] % 1 == 0.0:
            stack[-1] = int(stack[-1])
        stacklist.set(', '.join([str(x) for x in stack]))
        
def perform_factorial(): # Factorial.
    global stack
    if len(stack) < 1:
        tkinter.messagebox.showinfo("The error", "At least 1 element in the stack is required.")
    elif type(stack[-1]) != int:
        tkinter.messagebox.showinfo("The error", "The type of the argument is not an integer.")
    elif stack[-1] < 0:
        tkinter.messagebox.showinfo("The error", "Unable to factor a negative number.")
    elif stack[-1] > 25:
        tkinter.messagebox.showinfo("The error", "The number is too large.")
    else:
        stack[-1] = factorial(stack[-1])
        stacklist.set(', '.join([str(x) for x in stack]))



def create_button(text: str, command):
    return Button(mf, text = text, command = command, width = 5, height = 2)

def create_number_buttons():
    for i in range(9, -1, -3):
        for j in range(2, -1, -1):
            number = i-j
            column = (number-1) % 3
            row = 5-i//3
            if number == -2:
                number = 0
            button = create_button(str(number), lambda x=number: construct_number(x))
            button.grid(column=column, row=row)
        


# Drawing the grid.

create_number_buttons()

bt_plus = create_button('+', lambda x = '+': perform_operation(x))
bt_minus = create_button('-', lambda x = '-': perform_operation(x))
bt_multiplicate = create_button('*', lambda x = '*': perform_operation(x))
bt_divide = create_button('/', lambda x = '/': perform_operation(x))

bt_dot = create_button('.', construct_dot)
bt_factorial = create_button('!', perform_factorial)
bt_push = create_button('Push!', push)
bt_negative = create_button('neg', construct_minus)
bt_backspace = create_button('<-', goback)
bt_delete = create_button('<- (st)', delfromstack)

bt_plus.grid(column = 3, row = 2)
bt_minus.grid(column = 3, row = 3)
bt_multiplicate.grid(column = 3, row = 4)
bt_divide.grid(column = 3, row = 5)

bt_dot.grid(column = 1, row = 5)
bt_factorial.grid(column = 2, row = 5)
bt_push.grid(column = 3, row = 1)
bt_negative.grid(column = 2, row = 1)
bt_backspace.grid(column = 1, row = 1)
bt_delete.grid(column = 0, row = 1)
rt.mainloop() # The main loop of the application in order to make it more IDLE-friendly.