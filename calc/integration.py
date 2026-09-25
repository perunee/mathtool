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


def check_limits(a, b, low, high, strog):

    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("предел не является конечным числом")
    if a >= b:
        raise ValueError("начальный предел не меньше конечного")
    for i in a, b:
        if strog:
            outside = i < low or i > high
        else:
            outside = i <= low or i >= high
        if outside:
            raise ValueError("предел вне промежутка")


def check_steps(steps):
    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")


def integrate(F, a, b, steps):
    
    dx = (b - a) / steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        result += F(x) * dx
    return result