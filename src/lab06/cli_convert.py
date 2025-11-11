import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    subparsers = parser.add_subparsers(dest="command")

    p1 = subparsers.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = subparsers.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = subparsers.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.command == "json2csv":
        if args.input[-5:] != ".json":
            parser.error("Формат входного файла неверный. Используйте --help для помощи")
        elif args.output[-4:] != ".csv":
            parser.error("Формат выходного файла неверный. Используйте --help для помощи")
        else:
            try:
                json_to_csv(args.input, args.output)
            except FileNotFoundError:
                raise FileNotFoundError("Входной файл не найден.")
    elif args.command == "csv2json":
        if args.input[-4:] != ".csv":
            parser.error("Формат входного файла неверный. Используйте --help для помощи")
        elif args.output[-5:] != ".json":
            parser.error("Формат выходного файла неверный. Используйте --help для помощи")
        else:
            try:
                csv_to_json(args.input, args.output)
            except FileNotFoundError:
                raise FileNotFoundError("Входной файл не найден.")
    elif args.command == "csv2xlsx":
        if args.input[-4:] != ".csv":
            parser.error("Формат входного файла неверный. Используйте --help для помощи")
        elif args.output[-5:] != ".xlsx":
            parser.error("Формат выходного файла неверный. Используйте --help для помощи")
        else:
            try:
                csv_to_xlsx(args.input, args.output)
            except FileNotFoundError:
                raise FileNotFoundError("Входной файл не найден.")


if __name__ == "__main__":
    main()