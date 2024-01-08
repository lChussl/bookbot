def sort_on(d):
    return d["num"]


def sort_letters(letters):
    letters_list = []

    for letter in letters:
        letters_list.append({"letter": letter, "num": letters[letter]})

    letters_list.sort(key=sort_on, reverse=True)

    return letters_list


def count_letters(text):
    letters = {}

    for char in text:
        char = char.lower()

        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    return letters


def count_words(text):
    return len(text.split())


def read_book(book_path):
    with open(book_path) as f:
        return f.read()


def main():
    book_path = 'books/frankenstein.txt'
    file_content = read_book(book_path)

    print(f"-- Begin report of {book_path} --")

    print(f"{count_words(file_content)} words were found in the book")

    letters = count_letters(file_content)
    letters_sorted = sort_letters(letters)

    for letter in letters_sorted:
        if letter["letter"].isalpha():
            print(f"{letter['letter']} was found {letter['num']} times")

    print("-- End report --")


main()
