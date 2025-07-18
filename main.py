from stats import word_count
from stats import character_count
from stats import sort_dict

# Main function returns word count in document
def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_count(text)
    num_characters = character_count(text)
    print(f"{num_words} words found in the document")
    print(num_characters)

# Turns a file.txt into a string
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


       
main()



