import sys
from stats import get_book_txt, count_characters, get_sorted_char_stats, count_words

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_txt(book_path)
    word_count = count_words(text)
    char_counts = count_characters(text)
    sorted_stats = get_sorted_char_stats(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_stats:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()