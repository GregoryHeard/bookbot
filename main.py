from stats import get_word_count

# Main function returns word count in document
def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")

# Turns a file.txt into a string
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


       
main()



