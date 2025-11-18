import sys

sys.path.insert(0, "src")
import csv
from typing import Iterable, Sequence


def read_text(path: str, encoding: str = "utf-8") -> str:
    """Возвращает весь текст, находящийся в файле.

    :param path: путь до файла
    :type path: str
    :param encoding: кодировка текста (по умолчанию utf-8)
    :type encoding: str

    :raises FileNotFoundError: если файл не найден
    :raises UnicodeDecodeError: если кодировка не подходит

    :return: текст, находящийся в файле
    :rtype: str"""

    ret = ""
    with open(path, "r", encoding=encoding) as f:
        for line in f:
            ret = "\n".join([ret, line.strip()])
    return ret[1:]


def write_csv(
    rows: Iterable[Sequence], path: str, header: tuple[str, ...] | None = None
) -> None:
    """По указанному пути перезаписывает (или создаёт и записывает) файл формата csv с данными переданной таблицы.

    :param rows: данные таблицы
    :type rows: Iterable[Sequence]
    :param path: путь до файла
    :type path: str
    :param heading: строка заголовка (опционально)
    :type heading: tuple[str, ...]

    :raises ValueError: если строки таблицы имеют разную длину

    :return: функция записывает данные таблицы в файл
    :rtype: None"""

    table = []
    if header is not None:
        table.append(header)
    table.extend(list(rows))

    if len(table) > 0:
        row_len = len(table[0])
        for row_number, row in enumerate(table):
            if len(row) != row_len:
                raise ValueError(
                    f"Строки должны иметь одинаковую длину, но у строки {row_number} длина не совпадает с длиной строки 0."
                )

    with open(path, "w", encoding="utf-8") as f:
        w = csv.writer(f)
        for row in table:
            w.writerow(row)


if __name__ == "__main__":
    print(read_text("data/lab04/input.txt"))
    write_csv(
        [("мама", 3), ("папа", 1)], "data/lab04/check01.csv", ("слово", "частота")
    )
    write_csv(
        [("слово", "частота"), ("мама", 3), ("папа", 1)], "data/lab04/check02.csv"
    )
    write_csv([], "data/lab04/check03.csv", ("слово", "частота"))
    write_csv([], "data/lab04/check04.csv")
