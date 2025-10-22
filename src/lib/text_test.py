from test import test_print
from text import *

test_cases = {}
test_cases["normalize"] = [
    (["ПрИвЕт\nМИр\t"], "привет мир"),
    (["ёжик, Ёлка"], "ежик, елка"),
    (["Hello\r\nWorld"], "hello world"),
    (["  двойные   пробелы  "], "двойные пробелы")]
test_cases["tokenize"] = [
    (["привет мир"], ["привет", "мир"]),
    (["hello,world!!!"], ["hello", "world"]),
    (["по-настоящему круто"], ["по-настоящему", "круто"]),
    (["2025 год"], ["2025", "год"]),
    (["emoji 😀 не слово"], ["emoji", "не", "слово"]),
    (["-my, great--test-"], ["my", "great", "test"])]
test_cases["count_freq"] = [
    ([["a","b","a","c","b","a"]], {"a":3,"b":2,"c":1}),
    ([["bb","aa","bb","aa","cc"]], {"aa":2,"bb":2,"cc":1})]
test_cases["top_n"] = [
    ([{"a":3,"b":2,"c":1}, 2], [("a",3), ("b",2)]),
    ([{"aa":2,"bb":2,"cc":1}, 2], [("aa",2), ("bb",2)])]

test_print(test_cases["normalize"], normalize, 32)
test_print(test_cases["tokenize"], tokenize, 32)
test_print(test_cases["count_freq"], count_freq, 32)
test_print(test_cases["top_n"], top_n, 32)
