import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtool",
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command")

    solve = subparsers.add_parser(
        "solve", help="решение уравнения A*x^2+B*x+C = 0", allow_abbrev=False
    )
    solve.add_argument("-a", type=int, help="коэффициент A ")
    solve.add_argument("-b", type=int, help="коэффициент B ")
    solve.add_argument("-c", type=int, help="коэффициент C ")

    stats = subparsers.add_parser(
        "stats", help="показатели последовательности", allow_abbrev=False
    )
    stats.add_argument(
        "--input", help="файл с числами (без него числа читаются со стандартного ввода)"
    )

    
    series = subparsers.add_parser(
        "series", help="сумма ряда", allow_abbrev=False
    )
    series.add_argument("--func", required=True, help="какой ряд суммировать")
    group = series.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="сколько слагаемых сложить")
    group.add_argument("--eps", type=float, help="точность: считать, пока слагаемое >= eps")

    
    integrate = subparsers.add_parser(
        "integrate", help="численное интегрирование", allow_abbrev=False
    )
    integrate.add_argument("--func", required=True, help="какую функцию интегрировать")
    integrate.add_argument("--from", dest="start", type=float, required=True,
                           help="нижний предел")
    integrate.add_argument("--to", type=float, required=True, help="верхний предел")
    integrate.add_argument("--steps", type=int, required=True,
                           help="количество прямоугольников")

    return parser