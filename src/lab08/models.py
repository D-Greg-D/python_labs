from dataclasses import dataclass
from datetime import datetime
from datetime import date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except:
            raise ValueError("Формат даты должен быть YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA должен быть между 0 и 5")

    def age(self) -> int:
        self.__post_init__()
        b = self.birthdate
        today = date.today()
        return today.year - int(b.split("-")[0]) - (today.month < int(b.split("-")[1]) or (today.month == int(b.split("-")[1] and today.day < int(b.split("-")[2]))))

    def to_dict(self) -> dict:
        self.__post_init__()
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        fio = d.get("fio", "")
        birthdate = d.get("birthdate", "")
        group = d.get("group", "")
        gpa = d.get("gpa", 0)
        return cls(fio, birthdate, group, gpa)

    def __str__(self):
        return f"ФИО: {self.fio}\nДата рождения: {self.birthdate}\nГруппа: {self.group}\nGPA: {self.gpa}\n"
