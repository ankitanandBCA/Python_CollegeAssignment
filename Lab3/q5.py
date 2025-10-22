"""
Demonstrate the difference between mutable and immutable data types.
"""

# ==============================================================================
# --- Immutable Data Types ---
# ==============================================================================
# Immutable objects cannot be changed after they are created.
# Any "modification" results in a new object being created in memory.
# Examples: int, float, bool, string, tuple

print("--- Demonstrating IMMUTABLE Data Types ---")

# Example 1: String (immutable)
print("\n1. String (Immutable)")
original_string = "hello"
print(f"Original string: '{original_string}' with ID: {id(original_string)}")

# When we "modify" the string, Python creates a NEW string object.
print("...Concatenating ' world' to the string...")
original_string = original_string + " world"
print(f"Modified string: '{original_string}' with ID: {id(original_string)}")
print("--> The ID has changed, proving strings are immutable.")


# Example 2: Tuple (immutable)
print("\n2. Tuple (Immutable)")
my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple} with ID: {id(my_tuple)}")

# Trying to change an element of a tuple will raise a TypeError.
try:
    print("...Trying to change the first element to 99...")
    my_tuple[0] = 99
except TypeError as e:
    print(f"--> Caught an error: {e}")
    print("--> This error confirms that tuples are immutable.")





# ==============================================================================
# --- Mutable Data Types ---
# ==============================================================================
# Mutable objects can be changed in-place after they are created without
# creating a new object.
# Examples: list, dict, set

print("\n\n--- Demonstrating MUTABLE Data Types ---")

# Example 3: List (mutable)
print("\n3. List (Mutable)")
my_list = [10, 20, 30]
print(f"Original list: {my_list} with ID: {id(my_list)}")

# We can modify the list in-place using methods like append().
print("...Appending the number 40 to the list...")
my_list.append(40)
print(f"Modified list: {my_list} with ID: {id(my_list)}")
print("--> The ID is the same, proving lists are mutable.")

print("\n...Changing the first element to 99...")
my_list[0] = 99
print(f"Modified list: {my_list} with ID: {id(my_list)}")
print("--> The ID remains the same after in-place modification.")