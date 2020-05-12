from lessons.lesson_two.calculator import press, equal_press, clear, faculty, calc_sqrt


def get_button_def():
    return [
            [
                {'label': '7', 'command': lambda: press(7), 'column': 0, 'columnspan': 1},
                {'label': '8', 'command': lambda: press(8), 'column': 1, 'columnspan': 1},
                {'label': '9', 'command': lambda: press(9), 'column': 2, 'columnspan': 1},
                {'label': '+', 'command': lambda: press('+'), 'column': 3, 'columnspan': 1},
            ],
            [
                {'label': '4', 'command': lambda: press(4), 'column': 0, 'columnspan': 1},
                {'label': '5', 'command': lambda: press(5), 'column': 1, 'columnspan': 1},
                {'label': '6', 'command': lambda: press(6), 'column': 2, 'columnspan': 1},
                {'label': '-', 'command': lambda: press('-'), 'column': 3, 'columnspan': 1},
            ],
            [
                {'label': '1', 'command': lambda: press(1), 'column': 0, 'columnspan': 1},
                {'label': '2', 'command': lambda: press(2), 'column': 1, 'columnspan': 1},
                {'label': '3', 'command': lambda: press(3), 'column': 2, 'columnspan': 1},
                {'label': '*', 'command': lambda: press('*'), 'column': 3, 'columnspan': 1},
            ],
            [
                {'label': '0', 'command': lambda: press(0), 'column': 0, 'columnspan': 1},
                {'label': '.', 'command': lambda: press('.'), 'column': 1, 'columnspan': 1},
                {'label': '=', 'command': equal_press, 'column': 2, 'columnspan': 1},
                {'label': '/', 'command': lambda: press('/'), 'column': 3, 'columnspan': 1},
            ],
            [
                {'label': 'Clear', 'command': clear, 'column': 0, 'columnspan': 2},
                {'label': 'n!', 'command': faculty, 'column': 2, 'columnspan': 1},
                {'label': '√', 'command': calc_sqrt, 'column': 3, 'columnspan': 1},
            ],
        ]
