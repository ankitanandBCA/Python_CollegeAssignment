"""
write a program to chek weither a enter string is pangram,consogram,vowgram
"""
import string

# Define constants for vowels and the alphabet using sets for efficient lookups
VOWELS = {'a', 'e', 'i', 'o', 'u'}
ALPHABET = set(string.ascii_lowercase)

def is_pangram(text: str) -> bool:
    """
    Checks if a string is a pangram (contains every letter of the alphabet).
    """
    # Get all unique alphabetic characters from the text, in lowercase
    letters_in_text = {char for char in text.lower() if 'a' <= char <= 'z'}
    # Check if the set of all alphabet letters is a subset of the letters found
    return ALPHABET.issubset(letters_in_text)

def is_vowgram(text: str) -> bool:
    """
    Checks if a string is a vowgram (contains every vowel).
    """
    # Get all unique alphabetic characters from the text, in lowercase
    letters_in_text = {char for char in text.lower() if 'a' <= char <= 'z'}
    # Check if the set of vowels is a subset of the letters found
    return VOWELS.issubset(letters_in_text)

def is_consogram(text: str) -> bool:
    """
    Checks if a string is a consogram (each consonant appears at most once).
    """
    found_consonants = set()
    for char in text.lower():
        # Check if the character is a consonant
        if 'a' <= char <= 'z' and char not in VOWELS:
            # If we've already seen this consonant, it's not a consogram
            if char in found_consonants:
                return False
            # Otherwise, add it to our set of found consonants
            found_consonants.add(char)
    # If the loop completes, no consonants were repeated
    return True

def check_string_properties():
    """
    Main function to get user input and display the results.
    """
    print("--- String Property Checker (Pangram, Vowgram, Consogram) ---")
    user_input = input("Enter a string to check: ")

    if not user_input:
        print("Input cannot be empty.")
        return

    # Perform the checks
    is_pangram_result = is_pangram(user_input)
    is_vowgram_result = is_vowgram(user_input)
    is_consogram_result = is_consogram(user_input)

    # Display the results
    print("\n--- Results ---")
    print(f"Original String: '{user_input}'")
    print(f"Is it a Pangram?  (contains all 26 letters): {is_pangram_result}")
    print(f"Is it a Vowgram?  (contains all 5 vowels):  {is_vowgram_result}")
    print(f"Is it a Consogram? (no repeated consonants): {is_consogram_result}")


if __name__ == "__main__":
    check_string_properties()