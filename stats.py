def get_book_txt(path):
    with open(path, encoding="utf-8") as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():  # Solo contar letras
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def get_sorted_char_stats(char_counts):
    stats_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
    ]
    stats_list.sort(key=lambda x: x["num"], reverse=True)
    return stats_list