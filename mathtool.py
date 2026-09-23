# A*x**2+B*x+C = 0
import sys
from calc import equation

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
            print("Ошибка: коэффициент A не является целым числом",file=sys.stderr)
            sys.exit(1)
        try:
            B = int(input("Введите B: "))
        except ValueError:
            print("Ошибка: коэффициент B не является целым числом",file=sys.stderr)
            sys.exit(1)
        try:
            C = int(input("Введите C: "))
        except ValueError:
            print("Ошибка: коэффициент C не является целым числом",file=sys.stderr)
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
    
    kind, D, roots = equation.solve(A, B, C)

    print(kind, D, roots)
    

    

else:
    print("Ошибка: неверная команда",file=sys.stderr)
    sys.exit(1)