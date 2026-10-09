import math

MAX_STEPS = 100000

def f_ratio(x):
    return x / (x + 1)


def f_root(x):
    return math.sqrt(x ** 2 + 1)

def f_parab(x):
    return -x**2 + 4*x + 4/3


FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)", 0, 20, "rat"),
    "root": (f_root, "F(x) = sqrt(x^2 + 1)", -5, 5, "root"),
    "parab": (f_parab, "F(x) = -x^2 + 4x +4/3",-0.31, 4.31, "par")
}


def check_limits(start, to, low, high, func):

    if not (math.isfinite(start) and math.isfinite(to)):
        raise ValueError("предел не является конечным числом")
    if start >= to:
        raise ValueError("начальный предел не меньше конечного")
    for i in start, to:
        if func == "rat":
            outside = i < low or i > high
        elif func == "root":
            outside = i <= low or i >= high
        elif func == "par":
            outside = i < low or i >=high
        if outside:
            raise ValueError("предел вне промежутка")


def check_steps(steps):
    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")


def integrate(Function, start, to, steps):
    dx = (to - start) / steps
    result = 0
    for i in range(steps):
        x = start + i * dx
        result += Function(x) * dx
    return result
    