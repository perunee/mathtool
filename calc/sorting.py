from calc.arrays import MAX_COUNT,MAX_SEARCH,MAX_VALUE,MIN_VALUE
import random
import sys



def zapolnn(count , seed = None, low =MIN_VALUE, high =MAX_VALUE):
    if low > high:
        raise ValueError(f"Не верные границы. значение min должно быть меньше max")
    if int(low) < MIN_VALUE or high > MAX_VALUE:
        raise ValueError(f"Не верные границы. Максимальное ограничение от {MIN_VALUE} до {MAX_VALUE}")
    
    random.seed(seed)
    tt =[]
    i=1
    while i <= int(count):
        tt.append(random.randint(low, high))
        i +=1
    return tt

def get_array(input_path):
    
    if input_path is not None:
        try:
            with open(input_path, encoding="utf-8-sig") as handle:
                text = handle.read()
        except OSError:
            raise ValueError("файл не открывается")
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
            raise ValueError("файл не открываетсhhhhhh")



def poryadok(a,b,desc):
    if desc: return a < b
    else: return a > b 


def bubble(array,desc = False):
    n = len(array)
    for i in range(0, n - 2 +1):
        obmen = False
        for j in range(0, n - 2 - i +1):
            if poryadok(array[j] , array[j+1] , desc ):
                array[j], array[j+1] = array[j+1], array[j]
                
                obmen = True
        if obmen == False :
            break





METHODS = {
    "bubble": bubble,
    "selection":None,
    "insertion":None,
    "counting":None
}
