
input_string = input("Enter a string: ")

case_counts = {'UPPER_CASE': 0, 'LOWER_CASE': 0}


for char in input_string:
   
    if char.isupper():
        case_counts['UPPER_CASE'] += 1

    elif char.islower():
        case_counts['LOWER_CASE'] += 1

print(f"Number of uppercase letters: {case_counts['UPPER_CASE']}")
print(f"Number of lowercase letters: {case_counts['LOWER_CASE']}")
print(f"Final counts in dictionary: {case_counts}")