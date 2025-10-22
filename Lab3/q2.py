"""
Demonstrates common string methods: replace(), split(), lower(), and upper().
"""

# A sample string to work with
original_string = "Python is a Versatile and Powerful Language"
print(f"Original String: '{original_string}'\n")






# 1. replace(): Returns a new string where a specified value is replaced with another value.
print("--- 1. replace() ---")
replaced_string = original_string.replace("Versatile", "Fun")
print(f"After replacing 'Versatile' with 'Fun': '{replaced_string}'")
print("-" * 20 + "\n")






# 2. split(): Splits the string at the specified separator and returns a list of strings.
print("--- 2. split() ---")
word_list = original_string.split(" ")
print(f"String split by space: {word_list}")








# Example with a different separator
csv_string = "apple,banana,cherry"
print(f"\nAnother example string: '{csv_string}'")
csv_list = csv_string.split(',')
print(f"String split by comma: {csv_list}")
print("-" * 20 + "\n")







# 3. lower(): Converts the entire string to lowercase.
print("--- 3. lower() ---")
lower_case_string = original_string.lower()
print(f"String in lowercase: '{lower_case_string}'")
print("-" * 20 + "\n")









# 4. upper(): Converts the entire string to uppercase.
print("--- 4. upper() ---")
upper_case_string = original_string.upper()
print(f"String in uppercase: '{upper_case_string}'")
print("-" * 20 + "\n")