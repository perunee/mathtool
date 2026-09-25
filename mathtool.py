# A*x**2+B*x+C = 0

import sys
from calc import equation, stats, series, integration
from cli import build_parser

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

    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1



def handle_integrate(args):
    function, formula, low, high, closed = integration.FUNCTIONS[args.func]

    integration.check_limits(args.start, args.to, low, high, closed)
    integration.check_steps(args.steps)
    result = integration.integrate(function, args.start, args.to, args.steps)

    print(formula)
    print(f"Значение интеграла: {result}")
    return 0



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
    if all(v is None for v in given):
        args.a = int(input("Введите A: "))   
        args.b = int(input("Введите B: "))
        args.c = int(input("Введите C: "))
    elif any(v is None for v in given):
        raise ValueError("коэффиценты не все")
    equation.max_value({"A":args.a , "B": args.b, "C": args.c})
    kind, D, roots = equation.solve(args.a, args.b, args.c)
    print(kind, D, roots) 
    return 0





if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))