import argparse
from src.lib.text import normalize, tokenize, count_freq, top_n

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Вывести топ самых частых слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5, help="Количество слов в топе")

    args = parser.parse_args()
    
    text = []
    try:
        with open(args.input, "r") as f:
            for line in f:
                text.append(line)
    except FileNotFoundError:
        raise FileNotFoundError("Входной файл не найден")

    if args.command == "cat":
        for line_number, line in enumerate(text):
            if args.n:
                print(line_number + 1, line)
            else:
                print(line)
            
    elif args.command == "stats":
        top = top_n(count_freq(tokenize(normalize("\n".join(text)))), args.top)
        
        print(f"Топ-{args.top}:")
        
        width = 5
        for item in top:
            width = max(width, len(item[0]))
        
        print(f"{"слово":<{width}} | частота")
        print("-" * (width + 10))
        for item in top:
            print(f"{item[0]:<{width}} | {item[1]}")


if __name__ == "__main__":
    main()