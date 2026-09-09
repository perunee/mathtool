# A*x**2+B*x+C = 0
import sys
import math

max_value = 10000 


if len(sys.argv)-1 == 0 or sys.argv[1] == "--help":

    print('mathtool - решение уравнения вида A*x^2+B*x+C = 0\n'
        '\nИспользование: \n \n   python mathtool.py                         вывод справки\n   python mathtool.py --help                  вывод справки'
        '\n   python mathtool.py solve                   ввод коэффициентов с клавиатуры \n   python mathtool.py solve -a X -b X -c X    решение с задаными коэффициентами' \
        '\n\nКоэффициенты A, B, С - целые числа, по модулю не превышающие 10000')
    sys.exit(0)


elif sys.argv[1] == "solve":

    if len(sys.argv)-1 ==1:
        try:
            A = int(input("Введите A: "))
        except ValueError:
            print("Ошибка: коэффициент не является целым числом",file=sys.stderr)
            sys.exit(1)
        try:
            B = int(input("Введите B: "))
        except ValueError:
            print("Ошибка: коэффициент не является целым числом",file=sys.stderr)
            sys.exit(1)
        try:
            C = int(input("Введите C: "))
        except ValueError:
            print("Ошибка: коэффициент не является целым числом",file=sys.stderr)
            sys.exit(1)

    elif len(sys.argv) -1 == 7 and (sys.argv[2] =='-a' and sys.argv[4] =='-b' and sys.argv[6] =='-c'):
        try:
            A = int(sys.argv[3])
            B = int(sys.argv[5])
            C = int(sys.argv[7])
        except ValueError:
            print("Ошибка: числа должны быть целыми",file=sys.stderr)
            sys.exit(1)  

    else:
        print("Ошибка: неверная команда",file=sys.stderr)
        sys.exit(1)


    if abs(A) > max_value or abs(B) > max_value or abs(C) > max_value:
        print("Ошибка: значение вне допустимого диапазона",file=sys.stderr)
        sys.exit(1)


    if A == 0:
        if B != 0:
            print("Уравнение линейное")
            x = -C/B
            print(f"x = {x:.3f}")
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
            print("Действительных корней нет")

else:
    print("Ошибка: неверная команда",file=sys.stderr)
    sys.exit(1)