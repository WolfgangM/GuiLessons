import math
from tkinter import *

from lessons.lesson_two.button_def import get_button_def
from page import Page

calculator_expr = ""
calculator_equation = None


def faculty():
    global calculator_expr
    global calculator_equation

    try:

        calculator_expr = math.factorial(int(calculator_expr))
        calculator_equation.set(calculator_expr)

    except:
        calculator_equation.set(" error ")
        calculator_expr = ""


def calc_sqrt():
    global calculator_expr
    global calculator_equation

    try:

        calculator_expr = math.sqrt(int(calculator_expr))
        calculator_equation.set(calculator_expr)

    except:
        calculator_equation.set(" error ")
        calculator_expr = ""


def clear():
    global calculator_expr
    global calculator_equation

    calculator_equation.set("")
    calculator_expr = ""


def equal_press():
    global calculator_expr
    global calculator_equation

    try:

        total = str(eval(calculator_expr))

        calculator_equation.set(total)
        calculator_expr = ""

    except:
        calculator_equation.set(" error ")
        calculator_expr = ""


def press(num):
    global calculator_expr
    global calculator_equation

    try:
        global calculator_expr

        calculator_expr = calculator_expr + str(num)
        calculator_equation.set(calculator_expr)

    except:
        calculator_equation.set(" error ")
        calculator_expr = ""


class Calculator(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        global calculator_expr
        global calculator_equation

        calculator_equation = StringVar()
        calculator_equation.set('enter your expression')

        expression_field = Entry(self, textvariable=calculator_equation)
        expression_field.grid(columnspan=4, ipadx=70)

        buttons = get_button_def()

        for row_id, button_row in enumerate(buttons):
            for cell_id, button_cell in enumerate(button_row):
                button_entry = buttons[row_id][cell_id]
                button = Button(self, text=button_entry['label'], fg='black', bg='red',
                                command=button_entry['command'], height=1, width=7)
                button.grid(
                    row=row_id + 1,
                    column=button_entry['column'],
                    columnspan=button_entry['columnspan'],
                    sticky=N + S + E + W,
                )
