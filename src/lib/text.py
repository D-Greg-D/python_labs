from test import test_print

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
       text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    while text.count("  ") > 0:
        text = text.replace("  ", " ")
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    while text.count("--") > 0:
        text = text.replace("--", " ")
    for letter in text:
        if not (letter.isalnum() or letter == "_" or letter == "-"):
            text = text.replace(letter, " ")
    splitted = text.split()
    ret = []
    for item in splitted:
        while item[0] == "-":
            item = item[1:]
        while item[-1] == "-":
            item = item[:-1]
        ret.append(item)
    return ret

def count_freq(tokens: list[str]) -> dict[str, int]:
    ret = {}
    for word in tokens:
        ret[word] = ret.get(word, 0) + 1
    return ret

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted = []
    for value in freq.items():
        sorted.append((-value[1], value[0]))
    sorted.sort()
    ret = []
    for value in sorted:
        ret.append((value[1], -value[0]))
    return ret[0: n]



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