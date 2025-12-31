from stats import count_words, count_characters, sort_character_counts

BOOK_PATH = "books/frankenstein.txt"

def get_book_text(filepath: str) -> str:
    """Reads a book file and returns the contents as a string."""
    with open(filepath, 'r') as file:
        contents = file.read()
    return contents

def main():
    print("============ BOOKBOT ============")

    book_contents = get_book_text(BOOK_PATH)
    print(f"Analyzing book found at {BOOK_PATH}...")

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