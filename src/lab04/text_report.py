import sys
sys.path.insert(0, "src")

if __name__ == "__main__":
    from lib.text import normalize, tokenize, count_freq, top_n
    from lab04.io_txt_csv import read_text, write_csv
    from lab03.text_stats import text_stats
    
    text = read_text("data/lab04/input.txt")
    table = top_n(count_freq(tokenize(normalize(text))))
    write_csv(table, "data/lab04/report.csv", ("слово", "частота"))
    text_stats(text)
