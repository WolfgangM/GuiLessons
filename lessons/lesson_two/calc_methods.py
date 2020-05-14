import math


def faculty(self):
    try:

        expr = math.factorial(int(self.calculator_expr))

        self.calculator_expr = expr
        self.calculator_equation.set(expr)

    except:
        self.calculator_equation.set(" error ")
        self.calculator_expr = ""

    return self


def calc_sqrt(self):
    try:

        expr = math.sqrt(int(self.calculator_expr))

        self.calculator_expr = expr
        self.calculator_equation.set(expr)

    except:
        self.calculator_equation.set(" error ")
        self.calculator_expr = ""

    return self


def clear(self):
    self.calculator_equation.set("")
    self.calculator_expr = ""

    return self


def equal_press(self):
    try:

        total = str(eval(self.calculator_expr))

        self.calculator_equation.set(total)
        self.calculator_expr = ""

    except:
        self.calculator_equation.set(" error ")
        self.calculator_expr = ""

    return self


def press(self, num):
    try:

        expr = self.calculator_expr + str(num)

        self.calculator_expr = expr
        self.calculator_equation.set(expr)

    except:

        self.calculator_equation.set(" error ")
        self.calculator_expr = ""

    return self
