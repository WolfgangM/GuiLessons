import csv
import os
from tkinter import *
from tkinter.ttk import *

from page import Page


def combo_select_cb(self: Page, box_one: Combobox, box_two: Combobox, selectable: Combobox, data: list) -> Page:
    value_one = box_one.get()
    value_two = box_two.get()

    if (
        value_one != value_two
        and value_one != '-'
        and value_two != '-'
        and value_one in selectable
        and value_two in selectable
    ):
        index_one = selectable.index(value_one)
        index_two = selectable.index(value_two)
        self.distance_equation.set(str(data[index_one][index_two]) + 'km')
    else:
        self.distance_equation.set('Choose two different cities')

    self.focus()

    return self


def reset_distance(self: Page, box_one: Combobox, box_two: Combobox) -> Page:
    self.distance_equation.set(self.equation_text)
    box_one.current(0)
    box_two.current(0)

    return self


class Distances(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.equation_text = 'Choose two different cities'
        self.distance_equation = StringVar()
        self.distance_equation.set(self.equation_text)

        # Setup field-rows grid
        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)
        self.grid_rowconfigure(2)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Read CSV file and create matrix
        path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(path, "distances.csv")
        file = open(file_path, 'rt', encoding='utf8')
        data_list = list(csv.reader(file))
        options = data_list[0]

        # Define callbacks
        current = self

        def combo_cb_one(_: Combobox) -> None:
            combo_select_cb(current, combo_one, combo_two, options, data_list)

        def combo_cb_two(_: Combobox) -> None:
            combo_select_cb(current, combo_one, combo_two, options, data_list)

        def reset_cb() -> None:
            reset_distance(current, combo_one, combo_two)

        # Create labels
        label_one = Label(self, text='City #1')
        label_two = Label(self, text='City #2')
        label_three = Label(self, text='Distance')

        # Create combobox-fields
        combo_one = Combobox(self, values=options, state="readonly")
        combo_two = Combobox(self, values=options, state="readonly")

        # Apply default values on combobox-fields
        combo_one.current(0)
        combo_two.current(0)

        # Bind select callbacks on combobox-fields
        combo_one.bind("<<ComboboxSelected>>", combo_cb_one)
        combo_two.bind("<<ComboboxSelected>>", combo_cb_two)

        # Create result-field and configure
        expr_field = Label(self, textvariable=self.distance_equation)
        # expr_field.configure(state='readonly')

        # Create reset button
        reset_button = Button(self, text='Reset', command=reset_cb, width=7)

        # Apply labels to frame-grid
        label_one.grid(row=0, column=0, sticky=N + W)
        label_two.grid(row=1, column=0, sticky=N + W)
        label_three.grid(row=2, column=0, sticky=N + W)

        # Apply combo-boxes to frame-grid
        combo_one.grid(row=0, column=1, columnspan=5, sticky=N + S + E + W)
        combo_two.grid(row=1, column=1, columnspan=5, sticky=N + S + E + W)

        # Apply expression-field to frame-grid
        expr_field.grid(row=2, column=1, columnspan=5, sticky=N + W)

        # Apply reset-button to frame-grid
        reset_button.grid(row=3, column=0, columnspan=6, ipadx=70, sticky=N + S + E + W)
