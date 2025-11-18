def min_max(
    nums: list[float | int],
) -> tuple[float | int, float | int] | type[ValueError]:
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


test_cases = {}
test_cases["min_max"] = [[1, 4.0, 6], [2, 0, 0, 6], [1], [1, 1], [22.17, 35, 40], []]
test_cases["unique_sorted"] = [[4], [], [5, 3.3, 2.8, -91, -5.2], [324, -324, 0]]
test_cases["flatten"] = [
    [4, 5],
    [[4], [5]],
    [(8, 0, 2), [4, 6], (3, 2)],
    [[1, 4], "it's a number trust me"],
    [(1), 2],
]

print("Тесты функции min_max\n")
for param in test_cases["min_max"]:
    print(f"{str(param):<32} -> {min_max(param)}")
print()

print("Тесты функции unique_sorted\n")
for param in test_cases["unique_sorted"]:
    print(f"{str(param):<32} -> {unique_sorted(param)}")
print()

print("Тесты функции flatten\n")
for param in test_cases["flatten"]:
    print(f"{str(param):<32} -> {flatten(param)}")
