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

def sort_on(item: str) -> int:
    """Helper function to get the count from a dictionary item"""
    return item['count']

def sort_character_counts(char_count: dict) -> list:
    """Accepts a dictionary and returns a list of dictionaries sorted by character count in descending order."""

    sorted_counts = []
    for char, count in char_count.items():
        sorted_counts.append({'character': char, 'count': count})

    sorted_counts.sort(key=sort_on, reverse=True)
    return sorted_counts