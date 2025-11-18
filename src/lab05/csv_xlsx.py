import sys

sys.path.insert(0, "")
from openpyxl import Workbook
import csv


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    """
    inputSize = True

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path, "r", encoding="utf-8") as fin:
        for row in csv.reader(fin):
            inputSize = False
            ws.append(row)
    if inputSize:
        raise ValueError("Пустой CSV")

    for column in ws.columns:
        # length = max(len(str(cell.value)) for cell in column)
        length = max(map(lambda cell: len(str(cell.value)), column))
        ws.column_dimensions[column[0].column_letter].width = max(8, length) * 1.2

    wb.save(xlsx_path)


if __name__ == "__main__":
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")
