import math

MAX_STEPS = 100000

def f_ratio(x):
    return x / (x + 1)


def f_root(x):
    return math.sqrt(x **2 + 1)



FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (f_root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}


def check_limits(start, to, low, high, is_ratio):

    if not (math.isfinite(start) and math.isfinite(to)):
        raise ValueError("предел не является конечным числом")
    if start >= to:
        raise ValueError("начальный предел не меньше конечного")
    for i in start, to:
        if is_ratio:
            outside = i < low or i > high
        else:
            outside = i <= low or i >= high
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
    