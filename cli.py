import argparse
from calc.sorting import METHODS

def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtool",
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command")

    solve = subparsers.add_parser(
        "solve", help="Решение уравнения A*x^2+B*x+C = 0", allow_abbrev=False
    )
    solve.add_argument("-a", type=int, help="Коэффициент A ")
    solve.add_argument("-b", type=int, help="Коэффициент B ")
    solve.add_argument("-c", type=int, help="Коэффициент C ")

    stats = subparsers.add_parser(
        "stats", help="Показатели последовательности", allow_abbrev=False
    )
    stats.add_argument(
        "--input", help="Файл с числами (без него числа читаются со стандартного ввода)"
    )

    
    series = subparsers.add_parser(
        "series", help="Сумма ряда", allow_abbrev=False
    )
    series.add_argument("--func", required=True, help="Какой ряд суммировать")
    group = series.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="Сколько слагаемых сложить")
    group.add_argument("--eps", type=float, help="Точность: считать, пока слагаемое >= eps")

    
    integrate = subparsers.add_parser(
        "integrate", help="Численное интегрирование", allow_abbrev=False
    )
    integrate.add_argument("--func", required=True, help="Какую функцию интегрировать")
    integrate.add_argument("--from", dest="start", type=float, required=True,help="Нижний предел")
    integrate.add_argument("--to", type=float, required=True, help="Верхний предел")
    integrate.add_argument("--steps", type=int, required=True,help="Количество прямоугольников")

    fill = subparsers.add_parser(
        "fill", help="Создание массива по зажаным параметрам", allow_abbrev=False
    )
    fill.add_argument("--count","-c", required=True, help="Количество элементов, от 1 до 1 000 000")
    fill.add_argument("--min", type=int, required=False)
    fill.add_argument("--max", type=int, required=False)
    fill.add_argument("--seed", type=int,required=False,help="Начальное значение генератора, целое число")
    fill.add_argument("--output","-o",required=False,help= "Файл для созданного массива")

    sort = subparsers.add_parser(
        "sort", help= f"Сортировка массива {len(METHODS)} методами по возрастанию или убыванию ", allow_abbrev=False
    )
    sort.add_argument("--method","-m",required=True,help="bubble, selection, insertion или counting")
    sort.add_argument("--order", required=False,help="asc — по возрастанию, desc — по убыванию")
    sort.add_argument("--input","-i",required=False,help="Файл с исходным массивом")
    sort.add_argument("--output","-o",required=False,help="Файл для отсортированного массива")
    
    search = subparsers.add_parser(
        "search", help="Поиск элемента в массиве", allow_abbrev=False
    )
    search.add_argument("--value","-v",required=True,help="Искомое целое число, модуль не больше 1000")
    search.add_argument("--input","-i",required=False,help="Файл с массивом по возрастанию")
    return parser