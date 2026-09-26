import math
import sys
MAX_VALUE = 10000
MAX_COUNT = 20



def read_numbers(source):
    numbers = []
    for line in source:
        
        for word in line.split():
            try:
                value = float(word)
            except ValueError:
                raise ValueError(f"{word} не является числом")
            
            numbers.append(value)
    return numbers


def get_numbers(input_path):
    
    if input_path is not None:
        try:
            with open(input_path, encoding="utf-8-sig") as handle:
                numbers = read_numbers(handle)
        except OSError:
            raise ValueError("файл не открывается")
    else:
        numbers = read_numbers(sys.stdin)

    chek_list(numbers)
    
    return numbers 


def chek_list(num):
    if len(num) == 0:
        raise ValueError('нет чисел')
    if len(num) > MAX_COUNT:
        raise ValueError(f'чисел больше{MAX_COUNT}')
    for i in num:
        if not math.isfinite(i):
            raise ValueError(f"{i} не является конечным числом")
        if abs(i) > MAX_VALUE: 
            raise ValueError(f'значение {i} вне диапозона')


def summa(num):
    result = 0
    for i in num:
        result += i
    return result

def mid(num):
    return summa(num)/len(num)

def summ_kv(num):
    result = 0
    for i in num:
        result += i**2
    return result

def mid_kv(num):
    return math.sqrt(summ_kv(num) / len(num))

def kv_otkl(num):
    mid_value = mid(num)
    result = 0
    for i in num:
        result += (i-mid_value)**2
    return result

def dispers(num):
    return kv_otkl(num) / len(num)

def sko(num):
    return math.sqrt(dispers(num))

def st_ot(num):# CTAHDAPTHOE OTKJIOHEHUE
    if len(num) < 2:
        return None
    return math.sqrt(kv_otkl(num)/(len(num)-1)) 


def minimum(num):
    result = num[0]
    for i in num:
        if i < result:
            result = i
    return result


def maximum(num):
    result = num[0]
    for i in num:
        if i > result:
            result = i
    return result


def count_pos(num):
    result = 0
    for i in num:
        if i > 0:
            result +=1
    return result

def count_neg(num):
    result = 0
    for i in num:
        if i < 0:
            result +=1
    return result