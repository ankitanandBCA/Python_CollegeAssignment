
input_string = input("Enter a string with letters and digits: ")

counts_dict = {'LETTERS': 0, 'DIGITS': 0}


for char in input_string:

    if char.isalpha():
        counts_dict['LETTERS'] += 1

    elif char.isdigit():
        counts_dict['DIGITS'] += 1

# Final counts ko print karein
print(f"\nTotal number of letters: {counts_dict['LETTERS']}")
print(f"Total number of digits: {counts_dict['DIGITS']}")
print(f"Final counts in dictionary: {counts_dict}")
