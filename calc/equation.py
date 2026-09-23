import math


def solve(A,B,C):

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
        x = -C / B
        return "Уравнение линейное", None, [x]