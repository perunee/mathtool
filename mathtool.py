# A*x**2+B*x+C = 0

import sys
from calc import equation
from cli import build_parser



def handle_solve(args):
    given = [args.a, args.b, args.c]
    if all(v is None for v in given):
        args.a = int(input("Введите A: "))   
        args.b = int(input("Введите B: "))
        args.c = int(input("Введите C: "))
    elif any(v is None for v in given):
        raise ValueError("коэффиценты не все")
    equation.MAX_VALUE({"A":args.a , "B": args.b, "C": args.c})
    kind, D, roots = equation.solve(args.a, args.b, args.c)
    print(kind, D, roots) 
    return 0

def main(argv):
    parser = build_parser()
    args = parser.parse_args(sys.argv[1:])
    
    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return handle_solve(args)
        
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))