from calc import arrays as a
import random

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

# обработчик fill:
#     проверить количество и границы значений
#     массив = заполнить(count, min, max, seed)
#     вывести массив или записать в --output

def read_massive(road):
    if road != None:
        road.open(path, encoding="utf-8-sig")
    else:
        pass
#         функция прочитать_массив(путь):
#     если путь задан: прочитать весь файл
#     иначе:
#         читать строки до EOF или строки, пустой после strip()
#         соединить прочитанные строки пробелами
#     заменить запятые пробелами; разделить текст на слова
#     преобразовать слова в целые числа
#     проверить количество и диапазон значений
#     вернуть список чисел
# Указание. Для чтения использовать open(path, encoding="utf-8-sig"), для записи — open(path, "w", encoding="utf-8"). Строка результата: " ".join(str(x) for x in values) + "\n". EOF при вызове input обрабатывается через EOFError. Подсказка ввода направляется в stderr.

