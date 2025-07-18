from stats import word_count
from stats import character_count
from stats import sort_dict
import sys
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

# Turns a file.txt into a string
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

# Main function returns report including total word count and individual character counts
def main():
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = word_count(text)
    num_characters = character_count(text)
    report_counts = sort_dict(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    index = 0
    for n in report_counts:
        char = report_counts[index]["char"]
        num = report_counts[index]["num"]
        index += 1
        if char.isalpha() == True:
            print(f"{char}: {num}")
    print("============= END ===============")
        

      
main()


