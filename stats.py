def count_words(text: str) -> int:
    """Accepts text and returns the total number of words."""
    return len(text.split())

def count_characters(text: str) -> dict:
    """Accepts text and returns the number of times each character appears."""
    char_count = {}

    for char in text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count