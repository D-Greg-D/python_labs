> # Даниль Григорьянц
>
> ### БИВТ-25-1

# Лабораторная работа 1

## Задание 1

```python
name = input()
age = int(input())

print("Привет, %s! Через год тебе будет %d." % (name, age + 1))
```

![Задание 1](./images/lab01/01_greeting.png)

## Задание 2

```python
a = float(input().replace(',', '.'))
b = float(input().replace(',', '.'))

sum = a + b
avg = sum / 2

print("sum=%.2f; avg=%.2f" % (sum, avg))
```

![Задание 2](./images/lab01/02_sum_avg.png)

## Задание 3

```python
price = float(input().replace(',', '.'))
discount = float(input().replace(',', '.'))
vat = float(input().replace(',', '.'))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print("База после скидки: %.2f ₽" % base)
print("НДС:               %.2f ₽" % vat_amount)
print("Итого к оплате:    %.2f ₽" % total)
```

![Задание 3](./images/lab01/03_discount_vat.png)

## Задание 4

```python
all_minutes = int(input())

hours = (all_minutes // 60) % 24
minutes = all_minutes % 60

print("%d:%02d" % (hours, minutes))
```

![Задание 4](./images/lab01/04_minutes_to_hhmm.png)

## Задание 5

```python
surname, name, father_name = input().split()

initials = surname[0] + name[0] + father_name[0] + '.'
full_name_len = len(surname) + len(name) + len(father_name) + 2

print("Инициалы: %s" % initials)
print("Длина (символов): %d" % full_name_len)
```

![Задание 5](./images/lab01/05_initials_and_len.png)

## Задание 6

```python
participants_number = int(input())

intramural = 0
extramural = 0

for i in range(participants_number):
    surname, name, age, participation_format = input().split()
    if participation_format == "True":
        intramural += 1
    else:
        extramural += 1

print(intramural, extramural)
```

![Задание 6](./images/lab01/06_lab.png)

## Задание 7

```python
code = input()

source = ""

for first_letter_number in range(len(code)):
    if code[first_letter_number].isupper():
        for second_letter_number in range(first_letter_number + 1, len(code)):
            if code[second_letter_number].isnumeric():
                for letter_number in range(first_letter_number, len(code), second_letter_number - first_letter_number + 1):
                    source += code[letter_number]
                    if code[letter_number] == '.':
                        break
                break
        break

print(source)
```

![Задание 7](./images/lab01/07_lecture_seems_to_be_cancelled.png)

# Лабораторная работа 2

## Проверка функций в каждом файле была реализована подобным кодом:
```python
test_cases = {}
test_cases["function_name"] = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]

print("Тесты функции function_name\n")
for param in test_cases["function_name"]:
    print(f"{str(param):<fancy_number} -> {function_name(param)}")
print()
```
`fancy_number` - это фиксированное для каждого файла число, а `{str(param):<fancy_number>}` выравнивает все ответы для простоты чтения.

## Задание 1

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int] | type[ValueError]:
    """Функция выводит минимум и максимум в списке или ValueError, если список пустой"""
    if len(nums) <= 0:
        return ValueError
    
    nums_min, nums_max = min(nums), max(nums)
    return (nums_min, nums_max)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Функция выводит отсортированный список различных элементов вводного списка"""
    return sorted(list(set(nums)))


def flatten(mat: list[list | tuple]) -> list | type[TypeError]:
    """Функция выводит "расплющенный" список списков/кортежей в один список по строкам или TypeError, если в списке встречается не список/кортеж"""
    ret = []
    for row in mat:
        if (not isinstance(row, list)) & (not isinstance(row, tuple)):
            return TypeError
        else:
            ret.extend(row)
    return ret
```

![Задание 1](./images/lab02/arrays.png)

## Задание 2

```python
def width(mat: list[list[float | int]]) -> int:
    """Функция выводит длину строки, если матрица прямоугольная, и -1, если она рваная"""
    if len(mat) == 0:
        return 0
    
    mat_width = len(mat[0])
    for mat_row in mat:
        if len(mat_row) != mat_width:
            return -1
    
    return mat_width


def transpose(mat: list[list[float | int]]) -> list[list[float | int]] | type[ValueError]:
    """Функция транспонирует матрицу или выводит ValueError, если матрица рваная"""
    mat_width = width(mat)
    if mat_width == -1:
        return ValueError
    transposed_mat = [[] for i in range(mat_width)]
    
    for row in mat:
        for column_number, value in enumerate(row):
            transposed_mat[column_number].append(value)
    
    return transposed_mat


def row_sums(mat: list[list[float | int]]) -> list[float] | type[ValueError]:
    """Функция считает суммы значений в строках матрицы или выводит ValueError, если матрица рваная"""
    sums = []
    mat_width = width(mat)
    if mat_width == -1:
        return ValueError
    
    for row in mat:
        sum = 0
        for number in row:
            sum += number
        sums.append(sum)
    
    return sums


def col_sums(mat: list[list[float | int]]) -> list[float] | type[ValueError]:
    """Функция считает суммы значений в столбцах матрицы или выводит ValueError, если матрица рваная"""
    transposed_mat = transpose(mat)
    if transposed_mat is ValueError:
        return ValueError
    return row_sums(transposed_mat)
```

Отдельно была вынесена функция `width`, объединяющая проверку матрицы на прямоугольность и нахождение длины её строки, поскольку её функционал используется в двух функциях, а также может быть использован в будущем.

![Задание 2](./images/lab02/matrix.png)

## Задание 3

```python
def format_record(rec: tuple[str, str, float]) -> str | type[ValueError] | type[TypeError]:
    """
    TypeError выводится в случае, если третье значение (GPA) не формата float
    ValueError выводится в случаях, если первое значение (ФИО) состоит из менее двух или более трёх слов или второе значение (название группы) пустое
    """
    if not isinstance(rec[2], float):
        return TypeError
    
    if rec[1] == "":
        return ValueError
    
    name = rec[0].split(" ")
    while "" in name:
        name.remove("")
    
    if len(name) <= 1:
        return ValueError
    elif len(name) > 3:
        return ValueError
    
    return_name = ""
    for part_number, part in enumerate(name):
        if part_number == 0:
            part = part.lower()
            part = "".join([part[0].upper(), part[1:]])
            return_name = "".join([return_name, part, " "])
        else:
            return_name = "".join([return_name, part[0].upper(), "."])
    
    return_group = "".join(["гр. ", rec[1].strip()])
    return_gpa = rec[2]
    return f"{return_name}, {return_group}, {return_gpa:.2f}"
```

![Задание 3](./images/lab02/tuples.png)

# Лабораторная работа 3

## Проверка функций в файлах была усовершенствованна с прошлой лабораторной работы.

Теперь для запуска и вывода результатов работы функций была реализована специальная функция `test_print`, находящаяся в файле `src/lib/test.py`, необходимая для красивого вывода данных:

```python
import unicodedata

def test_print(test_cases: list[tuple], func, side_size: int) -> bool:
    if not callable(func):
        print("Функцию невозможно вызвать")
        print()
        return False
    
    ret = True
    for value in test_cases:
        cur_side_size = side_size
        result = func(*value[0])
        input_values = ""
        if len(value[0]) == 1:
            input_values = str(value[0][0]).replace("\t", "\\t").replace("\r", "\\r").replace("\n", "\\n")
        else:
            input_values = str(value[0]).replace("\t", "\\t").replace("\r", "\\r").replace("\n", "\\n")[1:-1]
        
        for letter in input_values:
            if unicodedata.east_asian_width(letter) in ("F", "W"):
                cur_side_size -= 1
        
        if result != value[1]:
            ret = False
            print(f"Неверно: {input_values:<{cur_side_size}} -> {result}")
        else:
            print(f"Верно:   {input_values:<{cur_side_size}} -> {result}")
    print()
    return ret
```

## Задание A

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
       text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    while "  " in text:
        text = text.replace("  ", " ")
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    while "--" in text:
        text = text.replace("--", " ")
    for letter in text:
        if not (letter.isalnum() or letter == "_" or letter == "-"):
            text = text.replace(letter, " ")
    splitted = text.split()
    ret = []
    for item in splitted:
        while item[0] == "-":
            item = item[1:]
        while item[-1] == "-":
            item = item[:-1]
        ret.append(item)
    return ret

def count_freq(tokens: list[str]) -> dict[str, int]:
    ret = {}
    for word in tokens:
        ret[word] = ret.get(word, 0) + 1
    return ret

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted = []
    for value in freq.items():
        sorted.append((-value[1], value[0]))
    sorted.sort()
    ret = []
    for value in sorted:
        ret.append((value[1], -value[0]))
    return ret[0: n]
```

![Задание A](./images/lab03/text.png)

## Задание B

```python
import sys
sys.path.insert(0, "src")
from lib.text import *

def text_stats(in_text: str) -> None:
    in_text = normalize(in_text)
    tokens = tokenize(in_text)
    unique_words = count_freq(tokens)
    top_5 = top_n(unique_words)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(unique_words)}")
    print("Топ-5:")
    
    width = 5
    for item in top_5:
        width = max(width, len(item[0]))
    
    print(f"{"слово":<{width}} | частота")
    print("-" * (width + 10))
    for item in top_5:
        print(f"{item[0]:<{width}} | {item[1]}")


if __name__ == "__main__":
    text_stats(input())
```

![Задание B](./images/lab03/text_stats.png)

Проверка проводилась запуском программы напрямую командой `echo "какой-то текст" | python3 scr/text_stats.py"`

# Лабораторная работа 4

## Задание A

```python
import sys
sys.path.insert(0, "src")
import csv
from typing import Iterable, Sequence

def read_text(path: str, encoding: str = "utf-8") -> str:
    """Возвращает весь текст, находящийся в файле.
    
    :param path: путь до файла
    :type path: str
    :param encoding: кодировка текста (по умолчанию utf-8)
    :type encoding: str
    
    :raises FileNotFoundError: если файл не найден
    :raises UnicodeDecodeError: если кодировка не подходит
    
    :return: текст, находящийся в файле
    :rtype: str"""
    
    ret = ""
    with open(path, "r", encoding=encoding) as f:
        for line in f:
            ret = "\n".join([ret, line.strip()])
    return ret[1:]

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """По указанному пути перезаписывает (или создаёт и записывает) файл формата csv с данными переданной таблицы.
    
    :param rows: данные таблицы
    :type rows: Iterable[Sequence]
    :param path: путь до файла
    :type path: str | Path
    :param heading: строка заголовка (опционально)
    :type heading: tuple[str, ...]
    
    :raises ValueError: если строки таблицы имеют разную длину
    
    :return: функция записывает данные таблицы в файл
    :rtype: None"""
    
    p = Path(path)
    table = []
    if header is not None:
        table.append(header)
    table.extend(list(rows))
    
    if (len(table) > 0):
        row_len = len(table[0])
        for row_number, row in enumerate(table):
            if len(row) != row_len:
                raise ValueError(f"Строки должны иметь одинаковую длину, но у строки {row_number} длина не совпадает с длиной строки 0.")
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for row in table:
            w.writerow(row)

if __name__ == "__main__":
    print(read_text("data/lab04/input.txt"))
    write_csv([("мама", 3), ("папа", 1)], "data/lab04/check01.csv", ("слово", "частота"))
    write_csv([("слово", "частота"), ("мама", 3), ("папа", 1)], "data/lab04/check02.csv")
    write_csv([], "data/lab04/check03.csv", ("слово", "частота"))
    write_csv([], "data/lab04/check04.csv")
```

![Задание A](./images/lab04/io_txt_csv.png)

## Задание B

```python
import sys
sys.path.insert(0, "src")

if __name__ == "__main__":
    from lib.text import normalize, tokenize, count_freq, top_n
    from lab04.io_txt_csv import read_text, write_csv
    from lab03.text_stats import text_stats
    
    text = read_text("data/lab04/input.txt")
    table = top_n(count_freq(tokenize(normalize(text))))
    write_csv(table, "data/lab04/report.csv", ("слово", "частота"))
    text_stats(text)
```

![Задание B](./images/lab04/text_report.png)
