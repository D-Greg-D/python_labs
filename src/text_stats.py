import tokenize
from lib.text import *

in_text = input()
in_text = normalize(in_text)
tokens = tokenize(in_text)
unique_words = count_freq(tokens)
top_5 = top_n(unique_words)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(unique_words)}")
print("Топ-5:")

width = 5
for item in top_5:
    width = max(width, len(item[0]))

print(f"{"слово":<{width}} | частота")
print("-" * (width + 10))
for item in top_5:
    print(f"{item[0]:<{width}} | {item[1]}")
