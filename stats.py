def count_words(text):
    words = text.split()
    return len(words)


def count_each_letter(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
    return letter_count


def sort_on(items):
    return items["num"]


def sort_letters(letter_count):
    chars = [{"char": key, "num": value} for key, value in letter_count.items()]
    chars.sort(reverse=True, key=sort_on)
    return chars
