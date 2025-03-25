from stats import word_count, char_count, pretty_print
import sys

def get_book_text(file_path):
    contents = ""

    with open(file_path) as f:
        contents = f.read()
    return contents

def print_stats(file_path, word_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        print(f"{i["letter"]}: {i["value"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    


    #path_to_book = "books/frankenstein.txt"
    contents_of_book = get_book_text(path_to_book)
    book_word_count = word_count(contents_of_book)
    book_char_count = char_count(contents_of_book)
        
    #print(book_char_count)
    sorted_char_list = pretty_print(book_char_count)
    print_stats(path_to_book, book_word_count, sorted_char_list)
    #print(f"{book_word_count} words found in the document")
   # print(book_char_count)


main()