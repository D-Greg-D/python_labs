import pytest
import csv
import json
import sys

sys.path.insert(0, "")
from src.lab05.json_csv import json_to_csv, csv_to_json


@pytest.mark.parametrize(
    "data, expected_len, expected_keys, expected_rows",
    [
        (
            [
                {
                    "name": "Danil",
                    "type": "player",
                    "defeated Ender Dragon": True,
                    "game time": 95,
                    "loves": "building",
                    "pets": "wolves",
                },
                {
                    "name": "Vlad",
                    "type": "player",
                    "defeated Ender Dragon": True,
                    "game time": 75,
                    "loves": "speedrunning",
                },
                {
                    "name": "Rinal",
                    "type": "player",
                    "defeated Ender Dragon": False,
                    "game time": 40,
                    "loves": "mining",
                    "music": True,
                },
            ],
            3,
            {
                "defeated Ender Dragon",
                "game time",
                "loves",
                "music",
                "name",
                "pets",
                "type",
            },
            [
                {
                    "defeated Ender Dragon": "True",
                    "game time": "95",
                    "loves": "building",
                    "music": "",
                    "name": "Danil",
                    "pets": "wolves",
                    "type": "player",
                },
                {
                    "defeated Ender Dragon": "True",
                    "game time": "75",
                    "loves": "speedrunning",
                    "music": "",
                    "name": "Vlad",
                    "pets": "",
                    "type": "player",
                },
                {
                    "defeated Ender Dragon": "False",
                    "game time": "40",
                    "loves": "mining",
                    "music": "True",
                    "name": "Rinal",
                    "pets": "",
                    "type": "player",
                },
            ],
        ),
        ([], 0, {}, []),
    ],
)
def test_json_to_csv(tmp_path, data, expected_len, expected_keys, expected_rows):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == expected_len
    if len(rows) == 0:
        return
    assert expected_keys <= set(rows[0].keys())
    for i in range(len(rows)):
        assert expected_rows[i] == rows[i]


def test_csv_to_json(tmp_path):
    src = tmp_path / "cities.csv"
    dst = tmp_path / "cities.json"
    data = "name,type,population\nKochanovo,base,42\nFlower Lake,village,0\nBerezhnyovo,village,2"
    src.write_text(data)
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        ans = json.load(f)

    assert ans == [
        {"name": "Kochanovo", "type": "base", "population": "42"},
        {"name": "Flower Lake", "type": "village", "population": "0"},
        {"name": "Berezhnyovo", "type": "village", "population": "2"},
    ]
