from lessons.lesson_two.calc_methods import *


def get_button_def(self):
    self.button_definition = [
        [
            {'label': '7', 'command': lambda: press(self, 7), 'column': 0, 'columnspan': 1},
            {'label': '8', 'command': lambda: press(self, 8), 'column': 1, 'columnspan': 1},
            {'label': '9', 'command': lambda: press(self, 9), 'column': 2, 'columnspan': 1},
            {'label': '+', 'command': lambda: press(self, '+'), 'column': 3, 'columnspan': 1},
        ],
        [
            {'label': '4', 'command': lambda: press(self, 4), 'column': 0, 'columnspan': 1},
            {'label': '5', 'command': lambda: press(self, 5), 'column': 1, 'columnspan': 1},
            {'label': '6', 'command': lambda: press(self, 6), 'column': 2, 'columnspan': 1},
            {'label': '-', 'command': lambda: press(self, '-'), 'column': 3, 'columnspan': 1},
        ],
        [
            {'label': '1', 'command': lambda: press(self, 1), 'column': 0, 'columnspan': 1},
            {'label': '2', 'command': lambda: press(self, 2), 'column': 1, 'columnspan': 1},
            {'label': '3', 'command': lambda: press(self, 3), 'column': 2, 'columnspan': 1},
            {'label': '*', 'command': lambda: press(self, '*'), 'column': 3, 'columnspan': 1},
        ],
        [
            {'label': '0', 'command': lambda: press(self, 0), 'column': 0, 'columnspan': 1},
            {'label': '.', 'command': lambda: press(self, '.'), 'column': 1, 'columnspan': 1},
            {'label': '=', 'command': lambda: equal_press(self), 'column': 2, 'columnspan': 1},
            {'label': '/', 'command': lambda: press(self, '/'), 'column': 3, 'columnspan': 1},
        ],
        [
            {'label': 'Clear', 'command': lambda: clear(self), 'column': 0, 'columnspan': 2},
            {'label': 'n!', 'command': lambda: faculty(self), 'column': 2, 'columnspan': 1},
            {'label': '√', 'command': lambda: calc_sqrt(self), 'column': 3, 'columnspan': 1},
        ],
    ]

    return self
