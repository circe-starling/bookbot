import sys
from stats import *


def main():
    # path_to_file = "books/frankenstein.txt"
    # word_count = count_the_words(path_to_file)
    # char_counts = count_the_characters(path_to_file)

    #   print(f"Found {word_count} total words")
    # print(char_counts)
    # print(sort_the_char_count(path_to_file))

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report(sys.argv[1])


main()
