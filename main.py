import sys

from stats import count_each_letter, count_words, sort_letters


def get_book_text(book_filepath):
    with open(book_filepath, "r") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein_book_filepath = sys.argv[1]
    frankenstein_book_text = get_book_text(frankenstein_book_filepath)
    frankenstein_letter_count = count_each_letter(frankenstein_book_text)
    sorted_letter_count = sort_letters(frankenstein_letter_count)

    print("bookbot".upper().center(30, "="))
    print(f"Analyzing book found at {frankenstein_book_filepath}")
    print("word count".title().center(30, "-"))
    print("found".title(), count_words(frankenstein_book_text), "total words")
    print("character count".title().center(30, "-"))
    for character in sorted_letter_count:
        print(f"{character['char']}:", character["num"])


main()
