# open file
file_path = "books/frankenstein.txt"
word_count = None


def main():
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        items = return_letter_count(words)

        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count} words found in the document")
        for item in items:
            print(f"The {item[0]} character was found {item[1]} times")


def return_letter_count(words):
    letter_count = {}
    for word in words:
        lower_case_word = word.lower()
        for letter in lower_case_word:
            if letter in letter_count and letter.isalpha():
                letter_count[letter] += 1
            elif letter.isalpha():
                letter_count[letter] = 1
    return sort_dictionary(letter_count)


def sort_on(item):
    return item[1]


def sort_dictionary(dictionary):
    items = list(dictionary.items())
    items.sort(reverse=True, key=sort_on)
    return items


main()
