

def get_book_text(filepath: str):
    """Reads a book file and returns the contents as a string."""

    with open(filepath, 'r') as file:
        contents = file.read()
    return contents




def main():
    book_contents = get_book_test("books/frankenstein.txt")
    print(book_contents)

if __name__ == "__main__":
    main()