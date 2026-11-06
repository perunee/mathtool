import random


MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1000000
MAX_SEARCH = 1000

def zapolnn(count , seed = None, low =MIN_VALUE, high =MAX_VALUE):
    
    random.seed(seed)
    tt =[]
    i=1
    while i <= int(count):
        tt.append(random.randint(low, high))
        i += 1
    return tt


def get_array(input_path):
    
    if input_path is not None:
        try:
            with open(input_path, encoding="utf-8-sig") as handle:
                text = handle.read()
        except OSError:
            raise ValueError("Файл не открывается")
    else:
        lines = []
        while True:
            try:
                line = input()
                if not line.strip(): 
                    break
                lines.append(line)
            except EOFError:
                break
        text = " ".join(lines)

    text = text.replace(",","")
    word = text.split()
    try:
        numbers = [int(w) for w in word]
    except ValueError:
        raise ValueError("В данных есть не целые числа")
        
    return numbers

def save_array(input_path,numbers):
    result_str = " ".join(str(x) for x in numbers)
    if input_path is not None:
        try:
            with open(input_path,"w", encoding="utf-8") as handle:
                handle.write(result_str)
        except OSError:
            raise ValueError("Файл не открывается")
        print(f"Записано элементов: {len(numbers)} в файл {input_path}")
    # else:
    #     print(result_str)



def double_search(array, isk):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        if array[mid] == int(isk): return mid
        elif array[mid] < int(isk): left = mid + 1
        else: right = mid - 1
    return None 