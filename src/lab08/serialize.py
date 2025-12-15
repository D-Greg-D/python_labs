import json
import sys
sys.path.insert(0, "")
from src.lab08.models import Student

def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def students_from_json(path) -> list[Student]:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        data = [data]
    ret = []
    for info in data:
        student = Student(info.get("fio", ""), info.get("birthday", ""), info.get("group", ""), info.get("gpa", ""))
        student.__post_init__()
        ret.append(student)
    return ret

if __name__ == "__main__":
    students = students_from_json("data/lab08/students_input.json")
    for student in students:
        print(f"{student.__str__()}Возраст: {student.age()}\n")
    students_to_json(students, "data/lab08/students_output.json")
