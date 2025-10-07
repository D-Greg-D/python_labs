def format_record(rec: tuple[str, str, float]) -> str | type[ValueError] | type[TypeError]:
    if not isinstance(rec[2], float):
        """Неверный формат GPA"""
        return TypeError
    
    if rec[1] == "":
        """Название группы пустое"""
        return ValueError
    
    name = rec[0].split(" ")
    while "" in name:
        name.remove("")
    
    if len(name) <= 1:
        """Только фамилия"""
        return ValueError
    elif len(name) > 3:
        """Больше двух слов на имя и отчество"""
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

test_cases = {}
test_cases["format_record"] = [("Иванов Иван Иванович", "BIVT-25", 4.6), ("Петров Пётр", "IKBO-12", 5.0), ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999), ("Пупупушкин", "PK-00", 2.0), ("Михайлов Стас", "", 6.0), ("Колесников Денис", "LI-2", "5.0")]

print("Тесты функции format_record\n")
for param in test_cases["format_record"]:
    print(f"{str(param):<56} -> {format_record(param)}")