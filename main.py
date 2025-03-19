import sys
from stats import *

def get_book_text(path : str):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():

    if not len(sys.argv)==2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book=get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    words = get_num_words(book)
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    cha_dict = count_characters(book)
    sorted_charas = sort_dictionary(cha_dict)
    for item in sorted_charas:
        print(f"{item["cha"]}: {item["num"]}")
    print("============= END ===============")

main()