"""
use break , countinues and loop control based program
"""

# --- 1. Demonstrating 'break' statement ---

print("--- 1. Using 'break' to stop a loop ---")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
search_fruit = "cherry"

print(f"Searching for '{search_fruit}' in the list: {fruits}")
for fruit in fruits:
    if fruit == search_fruit:
        print(f"Found '{search_fruit}'! Stopping search.")
        break  # Exit the loop immediately
    print(f"Checking {fruit}...")
print("Loop finished (due to break or completion).")

# --- 2. Demonstrating 'continue' statement ---

print("\n--- 2. Using 'continue' to skip an iteration ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Printing odd numbers, skipping even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(f"Skipping even number: {num}")
        continue 
    print(f"Found odd number: {num}")
print("Loop finished.")

# --- 3. Demonstrating 'else' clause with 'for' loop ---

print("\n--- 3. Using 'else' with a 'for' loop (Search Example) ---")
items = ["pen", "notebook", "eraser"]
item_to_find_success = "notebook"
item_to_find_failure = "stapler"

print(f"Attempting to find '{item_to_find_success}' in {items}:")
for item in items:
    if item == item_to_find_success:
        print(f"Found '{item_to_find_success}'!")
        break  # Break out of the loop
else:
 
    print(f"'{item_to_find_success}' not found in the list.")

print(f"\nAttempting to find '{item_to_find_failure}' in {items}:")
for item in items:
    if item == item_to_find_failure:
        print(f"Found '{item_to_find_failure}'!")
        break  # This break will not be reached
else:
   
    print(f"'{item_to_find_failure}' not found in the list.")

# --- 4. Demonstrating 'else' clause with 'while' loop ---

print("\n--- 4. Using 'else' with a 'while' loop ---")
count = 0
while count < 3:
    print(f"While loop iteration: {count}")
    count += 1
else:
    print("While loop completed normally (count is no longer < 3).")