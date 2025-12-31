import sys
from stats import count_words, count_characters, sort_character_counts

def get_book_path() -> str:
    """Gets the file path of the book from the command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(filepath: str) -> str:
    """Reads a book file and returns the contents as a string."""
    with open(filepath, 'r') as file:
        contents = file.read()
    return contents

def main():
    book_path = get_book_path()
    print("============ BOOKBOT ============")

    book_contents = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    num_words = count_words(book_contents)
    print(f"Found {num_words} total words")

    character_counts = count_characters(book_contents)
    sorted_character_counts = sort_character_counts(character_counts)
    print("--------- Character Count -------")
    for dict in sorted_character_counts:
        char = dict['character']
        count = dict['count']
        if char.isalpha():
            print(f"{char}: {count}")
    
    

if __name__ == "__main__":
    main()