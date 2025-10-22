"""
Demonstrates string slicing, joining, repetition, concatenation, and formatting.
"""


base_string = "Hello, Python World!"
print(f"Base String: '{base_string}'\n")


print("--- 1. Slicing ---")
substring = base_string[7:13]
print(f"Slice from index 7 to 13: '{substring}'")

first_five = base_string[:5]  # Extracts "Hello"
print(f"Slice from the beginning (first 5 chars): '{first_five}'")

from_index_14 = base_string[14:]  # Extracts "World!"
print(f"Slice from index 14 to the end: '{from_index_14}'")
print("-" * 20 + "\n")




print("--- 2. Joining ---")
list_of_words = ["Python", "is", "awesome"]
joined_string = " ".join(list_of_words)
print(f"List to join: {list_of_words}")
print(f"Joined with a space: '{joined_string}'")

dashed_string = "-".join(list_of_words)
print(f"Joined with a dash: '{dashed_string}'")
print("-" * 20 + "\n")







print("--- 3. Repetition ---")
repeated_string = "Echo... " * 3
print(f"Repeating 'Echo... ' 3 times: '{repeated_string}'")
print("-" * 20 + "\n")






print("--- 4. Concatenation ---")
str1 = "Good"
str2 = " Morning"
greeting = str1 + str2
print(f"Concatenating '{str1}' and '{str2}': '{greeting}'")
print("-" * 20 + "\n")






print("--- 5. Formatting (with f-strings) ---")
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(f"Formatted string: '{formatted_string}'")
print("-" * 20 + "\n")