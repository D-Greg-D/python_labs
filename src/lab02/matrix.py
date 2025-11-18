def width(mat: list[list[float | int]]) -> int:
    """Функция выводит длину строки, если матрица прямоугольная, и -1, если она рваная"""
    if len(mat) == 0:
        return 0

    mat_width = len(mat[0])
    for mat_row in mat:
        if len(mat_row) != mat_width:
            return -1

    return mat_width


def transpose(
    mat: list[list[float | int]],
) -> list[list[float | int]] | type[ValueError]:
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


test_cases = {}
test_cases["transpose"] = [[[4]], [], [[4, 6], [4.2, 5]], [[9, 0, 1], [1, 4, 5]]]
test_cases["row_sums"] = [
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]],
    [[2, 3, 5], [7, 11, 13], [17, 19, 23]],
]
test_cases["col_sums"] = [
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]],
    [[2, 3, 5], [7, 11, 13], [17, 19, 23]],
]

print("Тесты функции transpose\n")
for param in test_cases["transpose"]:
    print(f"{str(param):<48} -> {transpose(param)}")
print()

print("Тесты функции row_sums\n")
for param in test_cases["row_sums"]:
    print(f"{str(param):<48} -> {row_sums(param)}")
print()

print("Тесты функции col_sums\n")
for param in test_cases["col_sums"]:
    print(f"{str(param):<48} -> {col_sums(param)}")
