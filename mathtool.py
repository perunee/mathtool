import sys
from calc import equation, stats, series, integration, sorting, arrays
from cli import build_parser
import time

REPORT = [
    ("Количество", len, "d"),
    ("Сумма", stats.summa, ".3f"),
    ("Ср. арифм.", stats.mid, ".3f"),
    ("Сумма кв.", stats.summ_kv, ".3f"),
    ("Ср. кв.", stats.mid_kv, ".3f"),
    ("Дисперсия", stats.dispers, ".3f"),
    ("СКО", stats.sko, ".3f"),
    ("Станд. откл.", stats.st_ot,".3f"),
    ("Наименьшее", stats.minimum, ".3f"),
    ("Наибольшее", stats.maximum, ".3f"),
    ("Положительных", stats.count_pos, "d"),
    ("Отрицательных", stats.count_neg, "d"),
]

def get_time(function, array, descending, func_name):
    start = time.perf_counter()
    res = function(array, descending)
    fin = time.perf_counter()
    func_time = fin - start
    print(f"Функция: {func_name}; время: {func_time: .6f}",file=sys.stderr)
    return res



def main(argv):
    parser = build_parser()
    args = parser.parse_args(sys.argv[1:])
    
    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return handle_solve(args)
        if args.command == "stats":
            return handle_stats(args)
        if args.command == "series":
            return handle_series(args)
        if args.command == "integrate":
            return handle_integrate(args)
        if args.command =="fill":
            return handle_fill(args)
        if args.command =="sort":
            return handle_sort(args)
        if args.command =="search":
            return handle_search(args)

    except (ValueError, OSError, KeyError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


def handle_sort(args):
    array = sorting.get_array(args.input)
    function = sorting.METHODS[args.method]
    descending = (args.order == "desc")
    get_time(function,array, descending, args.method)
    # function(array, descending)
    sorting.save_array(args.output, array)
    print("Массив отсортирован")
    return 0


def handle_search(args):
    
    if not (int(args.value) < arrays.MAX_SEARCH):
        raise ValueError("Искомое число больше максимального")
    array = sorting.get_array(args.input)
    for i in range(0,len(array)-1):
        if not(array[i] <= array[i+1]):
            raise ValueError("Масcив не отсортирован")
    
    indecs = sorting.double_search(array, args.value)
    if indecs == None: 
        print(f"Значение {args.value} не найдено")
        return 1
    print(f"Значение {args.value} имеет элемент с индексом {indecs+1}")
    return 0


def handle_fill(args):
    low = args.min if args.min is not None else arrays.MIN_VALUE
    high = args.max if args.max is not None else arrays.MAX_VALUE
    arr = sorting.zapolnn(args.count, args.seed, low=low, high=high)
    sorting.save_array(args.output, arr)
    return 0    

def handle_integrate(args):
    
    try :
    
        function, formula, low, high, is_ratio = integration.FUNCTIONS[args.func]
        
        integration.check_limits(args.start, args.to, low, high, is_ratio)
        integration.check_steps(args.steps)
        result = integration.integrate(function, args.start, args.to, args.steps)

        print(formula)
        print(f"Значение интеграла: {result:.3f}")
        return 0
    
    except KeyError:
       raise KeyError(f"Неверное значение --func: ({args.func})")


def handle_series(args):
    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        series.check_terms(args.terms)
        result = series.sum_by_count(term, args.terms)
        count = args.terms
    else:
        series.check_eps(args.eps)
        result, count = series.sum_by_eps(term, args.eps)

    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")
    return 0


def handle_stats(args):
    numbers = stats.get_numbers(args.input)
    for label, function, form in REPORT:
        value = function(numbers)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    return 0
    



def handle_solve(args):
    given = [args.a, args.b, args.c]
    if all(i is None for i in given):
        args.a = equation.intABC("A")  
        args.b = equation.intABC("B") 
        args.c = equation.intABC("C") 
    elif any(i is None for i in given):
        raise ValueError("Укажите или все коэфиценты, или не одного")
    equation.max_value({"A":args.a , "B": args.b, "C": args.c})
    kind, D, roots = equation.solve(args.a, args.b, args.c)
    if D:
        if len(roots) == 2:
            print(kind, D, f"x1={roots[0]:.3f} x2={roots[1]:.3f}") 
        elif len(roots)==1:
            print(kind, D, f"x={roots[0]:.3f}")
        else: 
            print(kind, D, "нет действительных корней")
    else:
        print(kind,f"x={roots[0]:.3f}")
    return 0





if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))