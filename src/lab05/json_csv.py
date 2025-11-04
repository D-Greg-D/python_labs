import sys
sys.path.insert(0, "")
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Кодировка UTF-8. Порядок колонок — алфавитный.
    """
    with open(json_path, "r", encoding="utf-8") as fin:
        jsonin = json.load(fin)
    if isinstance(jsonin, dict):
        jsonin = [jsonin]
    elif not isinstance(jsonin, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    header = []
    for item in jsonin:
        if not isinstance(item, dict):
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        header.extend(item.keys())
    header = sorted(list(set(header)))
        
    with open(csv_path, "w", encoding="utf-8") as fout:
        csvout = csv.DictWriter(fout, fieldnames=header)
        csvout.writeheader()
        for entry in jsonin:
            csvout.writerow(entry)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    """
    with open(csv_path, "r", encoding="utf-8") as fin:
        csvin = list(csv.DictReader(fin))
        if len(csvin) == 0:
            raise ValueError("Пустой CSV")
        with open(json_path, "w", encoding="utf-8") as fout:
            json.dump(csvin, fout, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    json_to_csv("data/lab05/samples/people-1.json", "data/lab05/out/people-1.csv")
    json_to_csv("data/lab05/samples/people-2.json", "data/lab05/out/people-2.csv")
    csv_to_json("data/lab05/samples/cities.csv", "data/lab05/out/cities.json")
