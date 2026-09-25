import math

MAX_VALUE = 10000

def max_value(coefficientes):
    for name, value in coefficientes.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"значение коэффициента {name} вне допустимого диапазона")
    if coefficientes["A"]== 0 and coefficientes["B"]==0:
        raise ValueError("ОШИБКА: A и B не могут одновременно быть равны нулю")

def solve(A,B,C):
    max_value({"A": A, "B": B, "C": C})

    if A != 0:
        D = B**2 - 4 * A * C
        if D > 0:
            x1 = (-B + math.sqrt(D))/(2*A)
            x2 = (-B - math.sqrt(D))/(2*A)
            return "Уравнение квадратное",D,[x1,x2]
        
        elif D == 0:
            x = -B/(2*A)
            return "Уравнение квадратное",D,[x]
            
        else:
            return "Уравнение квадратное",D,[]
    else:
        if B!= 0:
            x = -C / B
            return "Уравнение линейное", None, [x]




        
def intABC(n):
    try:
        return int(input(f"Введите {n}: "))
    except ValueError:
        raise ValueError(f"коэффициент {n} не является целым числом")