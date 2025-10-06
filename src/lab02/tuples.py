def format_record(rec: tuple[str, str, float]) -> str | type[ValueError]:
    name = rec[0].split(' ')
    if len(name) <= 1:
        return ValueError
    
    return_name = name[0] + ' ' + name[1][0] + '.' + name[2][0] + '.'
    return_group = 'гр. ' + rec[1]
    return_gpa = str(round(rec[2], 2))
    return ", ".join([return_name, return_group, return_gpa])

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
