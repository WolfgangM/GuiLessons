import math

from page import Page


def faculty(self: Page) -> Page:
    try:

        expr = math.factorial(int(self.calculator_expr))

        self.calculator_expr = expr
        self.equation.set(expr)

    except:
        self.equation.set(" error ")
        self.calculator_expr = ""

    return self


def calc_sqrt(self: Page) -> Page:
    try:

        expr = math.sqrt(int(self.calculator_expr))

        self.calculator_expr = expr
        self.equation.set(expr)

    except:
        self.equation.set(" error ")
        self.calculator_expr = ""

    return self


def clear(self: Page) -> Page:
    self.equation.set("")
    self.calculator_expr = ""

    return self


def equal_press(self: Page) -> Page:
    try:

        total = str(eval(self.calculator_expr))

        self.equation.set(total)
        self.calculator_expr = ""

    except:
        self.equation.set(" error ")
        self.calculator_expr = ""

    return self


def press(self: Page, num: int) -> Page:
    try:

        expr = self.calculator_expr + str(num)

        self.calculator_expr = expr
        self.equation.set(expr)

    except:

        self.equation.set(" error ")
        self.calculator_expr = ""

    return self
