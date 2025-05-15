from stats import get_char_count, get_word_count, sort_dict
import sys

def get_book_text(fp):
    with open(fp) as file:
        return file.read()

def main():
    fp = None
    if len(sys.argv) == 2:
        fp = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(fp)
    char_dict = get_char_count(text)
    char_dict_list = sort_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fp}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")

    for dict in char_dict_list:
        char = None
        num = None
        for key, val in dict.items():
           if char == None:
               char = val
           else:
                num = val
        if str(char).isalpha():
            print(f"{char}: {num}")


    print("============= END ===============")

main()
