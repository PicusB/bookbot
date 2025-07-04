from stats import count_words
from stats import count_characters
from stats import sort_character_dictionary
from report import printreport

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    book_word_count = count_words(book_text)
    print(f"{book_word_count} words found in the document")
    letter_dictionary = count_characters(book_text)
    printreport(book_word_count, sort_character_dictionary(letter_dictionary), "books/frankenstein.txt")

main()
