import csv
import sys
sys.path.insert(0, "")
from src.lab08.models import Student

class Group:
    path: str
    
    def __init__(self, csv_path):
        self.path = csv_path
    
    def _read_all(self) -> list:
        ret = []
        with open(self.path, "r", encoding="utf-8") as file:
            ret = list(csv.DictReader(file))
        for student in ret:
            try:
                student["gpa"] = float(student.get("gpa", 0))
            except:
                raise ValueError("GPA должен быть вещественным числом")
        return ret
    
    def _write(self, rows):
        with open(self.path, "w", encoding="utf-8") as file:
            w = csv.DictWriter(file, fieldnames=["fio", "birthdate", "group", "gpa"])
            w.writeheader()
            for student in rows:
                w.writerow(student)
    
    def list(self) -> list[Student]:
        ret = []
        for student in self._read_all():
            ret.append(Student.from_dict(student))
        return ret
    
    def add(self, student):
        table = self._read_all()
        table.append(student.to_dict())
        self._write(table)
    
    def find(self, substr):
        ret = []
        for student in self.list():
            if substr in student.fio:
                ret.append(student)
        return ret
    
    def remove(self, fio):
        table = self._read_all()
        for student in table:
            if student.get("fio", "") == fio:
                table.remove(student)
        self._write(table)

    def update(self, fio, **fields):
        table = self._read_all()
        for student in table:
            if student.get("fio", "") == fio:
                student["fio"] = fields.get("fio", student.get("fio", ""))
                student["birthdate"] = fields.get("birthdate", student.get("birthdate", ""))
                student["group"] = fields.get("group", student.get("group", ""))
                student["gpa"] = fields.get("gpa", student.get("gpa", 0))
        self._write(table)

if __name__ == "__main__":
    group = Group("data/lab09/students.csv")
    print(group.find("Мордашкин")[0].__str__())
    group.remove("Мордашкин Карим Камилевич")
    group.add(Student("Ахметов Ранэль Риналевич", "2005-01-01", "11А", 4.7))
    group.update("Таракашкин Владимир Владиславович", gpa=4.5, group="Выпуск")