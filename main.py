def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text_as_string):
    book_words = book_text_as_string.split()
    book_word_count = len(book_words)
    return book_word_count

def main():
    book_word_count = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{book_word_count} words found in the document")

main()
