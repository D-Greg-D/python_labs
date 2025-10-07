# **Лабораторные работы Даниля Григорьянца (БИВТ-25-1)**

# Лабораторная работа 2

## Задание 1

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int] | type[ValueError]:
    if len(nums) <= 0:
        return ValueError
    
    nums_min, nums_max = min(nums), max(nums)
    return (nums_min, nums_max)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(list(set(nums)))


def flatten(mat: list[list | tuple]) -> list | type[TypeError]:
    ret = []
    for row in mat:
        if (not isinstance(row, list)) & (not isinstance(row, tuple)):
            return TypeError
        else:
            ret.extend(row)
    return ret


test_cases = {}
test_cases["min_max"] = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]
test_cases["unique_sorted"] = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]
test_cases["flatten"] = [[[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]], [[1, 2], "ab"]]

for param in test_cases["min_max"]:
    print(min_max(param))

for param in test_cases["unique_sorted"]:
    print(unique_sorted(param))

for param in test_cases["flatten"]:
    print(flatten(param))
```

## Задание 2

```python
def width(mat: list[list[float | int]]) -> int:
    if len(mat) == 0:
        return 0
    
    mat_width = len(mat[0])
    for mat_row in mat:
        if len(mat_row) != mat_width:
            return -1
    
    return mat_width


def transpose(mat: list[list[float | int]]) -> list[list[float | int]] | type[ValueError]:
    mat_width = width(mat)
    if mat_width == -1:
        return ValueError
    transposed_mat = [[] for i in range(mat_width)]
    
    for row in mat:
        for column_number, value in enumerate(row):
            transposed_mat[column_number].append(value)
    
    return transposed_mat


def row_sums(mat: list[list[float | int]]) -> list[float] | type[ValueError]:
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
    transposed_mat = transpose(mat)
    if transposed_mat is ValueError:
        return ValueError
    return row_sums(transposed_mat)


test_cases = {}
test_cases["transpose"] = [[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]]
test_cases["row_sums"] = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]
test_cases["col_sums"] = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]

for param in test_cases["transpose"]:
    print(transpose(param))

for param in test_cases["row_sums"]:
    print(row_sums(param))

for param in test_cases["col_sums"]:
    print(col_sums(param))
```

## Задание 3

```python
def format_record(rec: tuple[str, str, float]) -> str | type[ValueError] | type[TypeError]:
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
    
    return_group = "".join(["гр. ", rec[1]])
    return_gpa = rec[2]
    return f"{return_name}, {return_group}, {return_gpa:.2f}"

test_cases = [("Иванов Иван Иванович", "BIVT-25", 4.6), ("Петров Пётр", "IKBO-12", 5.0), ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999), ("Пупупушкин", "PK-00", 2.0), ("Михайлов Стас", "", 6.0), ("Колесников Денис", "LI-2", "5.0")]
for param in test_cases:
    print(format_record(param))
```

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
