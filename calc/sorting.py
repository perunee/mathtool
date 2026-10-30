from calc import arrays as a
import random
import sys

MIN_VALUE = int(a.MIN_VALUE)
MAX_VALUE = int(a.MAX_VALUE)
MAX_COUNT = int(a.MAX_COUNT)
MAX_SEARCH = int(a.MAX_SEARCH)

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


def read_array(source):
    arr = []
    numbers = []
    while True:       
        input_num = input()
        if input_num == '':
            break
        else:
            arr.append(input_num)
    for line in arr:
        numbers.extend(line.split())
                
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    return numbers


def get_array(input_path):
    
    if input_path is not None:
        try:
            with open(input_path, encoding="utf-8-sig") as handle:
                numbers = read_array(handle)
        except OSError:
            raise ValueError("файл не открывается")
    else:
        numbers = read_array(sys.stdin)

def save_array(input_path):
    
    if input_path is not None:
        try:
            with open(input_path,"w", encoding="utf-8-sig") as handle:
                numbers = read_array(handle)
        except OSError:
            raise ValueError("файл не открываетсhhhhhh")



def poryadok(a,b,desc):
    if desc: return a<b
    else: return b<a


def bubble(array,desc = False):
    n = len(array)
    for i in range(0,n - 2 +1):
        obmen = False
        for j in range(0,n - 2 - i +1):
            if poryadok(i , j , desc ):
                a = array[j]
                array[j] = array[j+1]
                array[j+1] = a
                obmen = True
        if obmen == False :
            break