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
    