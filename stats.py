def count_words(book_text_as_string):
    book_words = book_text_as_string.split()
    book_word_count = len(book_words)
    return book_word_count

def count_characters(book_text_as_string):
    book_text_as_string = book_text_as_string.lower()
    letter_dictionary = []
    for character in book_text_as_string:
        if character.isalpha():
            char_found = False
            for entries in letter_dictionary:
                if entries["char"]==character:
                    entries["num"]+=1
                    char_found = True
                    break
            if not char_found:    
                letter_dictionary.append({"char" : character, "num" : 1})
    return letter_dictionary

def sort_on(items):
    return items["num"]

def sort_character_dictionary(character_dictionary):
    character_dictionary.sort(reverse=True, key=sort_on)
    return character_dictionary