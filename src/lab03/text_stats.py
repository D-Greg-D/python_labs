import sys
sys.path.insert(0, "src")
from lib.text import *

def text_stats(in_text: str) -> None:
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


if __name__ == "__main__":
    text_stats(input())