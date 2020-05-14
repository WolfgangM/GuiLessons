from tkinter import *
from lessons.lesson_two.button_def import get_button_def
from page import Page


class Calculator(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Define class-attributes
        self.button_definition = []
        self.calculator_expr = ""
        self.calculator_equation = StringVar()
        self.calculator_equation.set('enter your expression')

        # Get button definition array
        get_button_def(self)

        # Create and set expression field
        expression_field = Entry(self, textvariable=self.calculator_equation)
        expression_field.grid(columnspan=4, ipadx=70)

        # Create and set calculator buttons
        for row_id, button_row in enumerate(self.button_definition):

            for cell_id, button_cell in enumerate(button_row):
                button_entry = self.button_definition[row_id][cell_id]

                button = Button(self,
                                text=button_entry['label'],
                                fg='black',
                                bg='red',
                                command=button_entry['command'],
                                height=1,
                                width=7)

                button.grid(
                    row=row_id + 1,
                    column=button_entry['column'],
                    columnspan=button_entry['columnspan'],
                    sticky=N + S + E + W,
                )
