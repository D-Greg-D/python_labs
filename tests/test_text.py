import pytest
import sys

sys.path.insert(0, "")
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, casefold, yo2e, expected",
    [
        ("ПрИвЕт\nМИр\t", True, True, "привет мир"),
        ("ёжик, Ёлка", True, True, "ежик, елка"),
        ("Hello\r\nWorld", True, True, "hello world"),
        ("  двойные   пробелы  ", True, True, "двойные пробелы"),
        ("Ё выживет", True, False, "ё выживет"),
        ("БОЛЬШИЕ", False, True, "БОЛЬШИЕ"),
    ],
)
def test_normalize_basic(source, casefold, yo2e, expected):
    assert normalize(source, casefold=casefold, yo2e=yo2e) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("-my, great--test-", ["my", "great", "test"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
    ],
)
def test_count_freq(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
    ],
)
def test_top_n(source, n, expected):
    assert top_n(source, n) == expected
