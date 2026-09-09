# A*x**2+B*x+C = 0
import sys
import math

max_value = 10000 

try:
    A = int(input("Введите A"))
except ValueError:
    print("Ошибка: A должно быть целым числом",file=sys.stderr)
    sys.exit(1)
try:
    B = int(input("Введите B"))
except ValueError:
    print("Ошибка: B должно быть целым числом",file=sys.stderr)
    sys.exit(1)
try:
    C = int(input("Введите C"))
except ValueError:
    print("Ошибка: C должно быть целым числом",file=sys.stderr)
    sys.exit(1)


if abs(A) > max_value or abs(B) > max_value or abs(C) > max_value:
    print("Ошибка: значение вне допустимого диапозона",file=sys.stderr)
    sys.exit(1)


if A == 0:
    if B != 0:
        print("Уравнение Линейное")
        x = -C/B
        print(x)
    else:
        print("Ошибка: это не уравнение, неизвестное отсутствует",file=sys.stderr)
        sys.exit(1)
else:
    print("Уравнение квадратное")
    D = B**2 - 4 * A * C 
    print("Дискриминант: ",D)
    if D > 0:
        x1 = (-B + math.sqrt(D))/(2*A)
        x2 = (-B - math.sqrt(D))/(2*A)
        print(f"x1 = {x1:.3f}",f"x2 = {x2:.3f}")
    elif D == 0:
        x = -B/(2*A)
        print(f"x = {x:.3f}")
    else:
        print("Нет действительных корней")