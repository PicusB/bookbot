def printreport(word_count, sorted_character_count_list, book_path):
    header = "============ BOOKBOT ============"
    book_analysis = f"Analyzing book found at {book_path}"
    word_count_header ="----------- Word Count ----------"
    word_count_result = f"Found {word_count} total words"
    character_count_header = "--------- Character Count -------"
    end_of_report_marker = "============= END ==============="

    print(header)
    print(book_analysis)
    print(word_count_header)
    print(word_count_result)
    print(character_count_header)
    for character_count in sorted_character_count_list:
        print(f"{character_count["char"]}: {character_count["num"]}")
    print(end_of_report_marker)