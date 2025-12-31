def count_words(text: str) -> int:
    """Accepts text and returns the total number of words."""
    return len(text.split())


def get_book_text(filepath: str) -> str:
    """Reads a book file and returns the contents as a string."""

    with open(filepath, 'r') as file:
        contents = file.read()
    return contents

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_contents)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()