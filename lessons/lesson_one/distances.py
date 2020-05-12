import csv
import os
from tkinter import *
from tkinter.ttk import Combobox

from page import Page

distance_equation = None


def combo_select_cb(master, box_one, box_two, selectable, data):
    global distance_equation

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
        distance_equation.set(data[index_one][index_two] + 'km')
    else:
        distance_equation.set('Choose two different cities')

    master.focus()


def reset_distance(box_one, box_two):
    global distance_equation

    distance_equation.set('Choose two different cities')
    box_one.current(0)
    box_two.current(0)


class Distances(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        global distance_equation

        distance_equation = StringVar()
        distance_equation.set('Choose two different cities')

        path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(path, "distances.csv")
        file = open(file_path, 'rt', encoding='utf8')
        data_list = list(csv.reader(file))
        options = data_list[0]

        label_one = Label(self, text='City #1')
        label_one.grid(row=0, column=0, sticky=N + W)

        master = self

        def combo_callback(ignore):
            combo_select_cb(master, combo_one, combo_two, options, data_list)

        combo_one = Combobox(self, values=options, state="readonly")
        combo_one.grid(row=0, column=1, columnspan=3, sticky=N + S + E + W)
        combo_one.current(0)
        combo_one.bind("<<ComboboxSelected>>", combo_callback)

        label_two = Label(self, text='City #2')
        label_two.grid(row=1, column=0, sticky=N + W)

        combo_two = Combobox(self, values=options, state="readonly")
        combo_two.grid(row=1, column=1, columnspan=3, sticky=N + S + E + W)
        combo_two.current(0)
        combo_two.bind("<<ComboboxSelected>>", combo_callback)

        label_three = Label(self, text='Distance')
        label_three.grid(row=2, column=0, sticky=N + W)

        expression_field = Entry(self, textvariable=distance_equation)
        expression_field.configure(state='readonly')
        expression_field.grid(row=2, column=1, columnspan=3, ipadx=70, sticky=N + S + E + W)

        reset_button = Button(self, text='Reset', command=lambda: reset_distance(combo_one, combo_two), height=1, width=7)
        reset_button.grid(row=3, column=0, columnspan=4, ipadx=70, sticky=N + S + E + W)
