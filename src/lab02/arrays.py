def min_max(nums: list[float | int]) -> tuple[float | int, float | int] | type[ValueError]:
    if len(nums) <= 0:
        return ValueError
    
    min, max = nums[0], nums[0]
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    return (min, max)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(list(set(nums)))

def flatten(mat: list[list | tuple]) -> list | type[TypeError]:
    ret = []
    for sth in mat:
        if (not isinstance(sth, list)) & (not isinstance(sth, tuple)):
            return TypeError
        else:
            ret.extend(list(sth))
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
