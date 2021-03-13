"""
Write a function to count the letters in string
i.e. count alphabetical letters, not characters
- check if each char is a member (using in operator) of string.ascii_lowercase
- need to import string
- use char.lower() to ignore case
"""
import string

def count_letters(text):
    """Count the number of letters in text."""
    count = 0
    for char in text:
        if char.lower() in string.ascii_letters:
            count += 1
    return count
