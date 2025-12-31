from stats import count_words, count_characters

def get_book_text(filepath: str) -> str:
    """Reads a book file and returns the contents as a string."""
    with open(filepath, 'r') as file:
        contents = file.read()
    return contents

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    
    num_words = count_words(book_contents)
    print(f"Found {num_words} total words")

    character_counts = count_characters(book_contents)
    print("\nCharacter counts:")
    for char, count in character_counts.items():
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()