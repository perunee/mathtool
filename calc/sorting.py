from calc.arrays import MAX_VALUE, MIN_VALUE




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

def selection(array, desc = False):
    n = len(array)
    for i in range(0, n - 2 + 1):
        best = i
        for j in range(i + 1, n - 1 + 1):
            if poryadok(array[best],array[j],desc):
                best = j
        array[i],array[best] = array[best], array[i]

def insertion(array, desc = False):
    n = len(array)
    for i in range(1, n - 1 + 1):
            now = array[i]
            j = i 
            while (j > 0) and poryadok(array[j-1], now, desc):
                array[j] = array[j-1]
                j-=1
            array[j] = now

def counting(array, desc = False, min = MIN_VALUE, max = MAX_VALUE):
    count = [0]* (max - min + 1)
    for i in array:
        try:
            count[i - min] +=1
        except:
            print(f"значение {i} вне диавозона {max, min}")
            return 1
    k = 0
    nomer = range(max - min + 1)
    if desc:
        nomer = reversed(nomer)
    for i in nomer:
        for n in range(count[i]):
            array[k] = i + min
            k+=1

    
METHODS = {  #на 30 000 эл
    "bubble": bubble, #44сек
    "selection":selection, #17сек
    "insertion":insertion, #14сек
    "counting":counting #<1сек
}
