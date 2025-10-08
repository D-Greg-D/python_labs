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


test_cases = {}
test_cases["min_max"] = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]
test_cases["unique_sorted"] = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]
test_cases["flatten"] = [[[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]], [[1, 2], "ab"]]

print("Тесты функции min_max\n")
for param in test_cases["min_max"]:
    print(f"{str(param):<24} -> {min_max(param)}")
print()

print("Тесты функции unique_sorted\n")
for param in test_cases["unique_sorted"]:
    print(f"{str(param):<24} -> {unique_sorted(param)}")
print()

print("Тесты функции flatten\n")
for param in test_cases["flatten"]:
    print(f"{str(param):<24} -> {flatten(param)}")
