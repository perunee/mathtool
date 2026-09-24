import math
max_value = 10000

def MAX_VALUE(coefficientes):
    for name, value in coefficientes.items():
        if abs(value) > max_value:
            raise ValueError(f"значение коэффициента {name} вне допустимого диапазона")
    if coefficientes["A"]== 0 and coefficientes["B"]==0:
        raise ValueError("ОШИБКА: A и B не могут одновременно быть равны нулю")

def solve(A,B,C):
    for i in A,B,C:
        MAX_VALUE(i)

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
        
                