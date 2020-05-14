import tkinter


class Page(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)

        self.calculator_equation = None
        self.equation_text = None
        self.distance_equation = None

    def show(self):
        self.lift()
