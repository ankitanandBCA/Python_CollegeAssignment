"""
write a program to read and print value of variable to different data types
"""

def demonstrate_data_types():
    """
    Reads a value from the user and attempts to print it as different data types.
    """
    # 1. Read input as a string (this is its raw form)
    user_input = input("Enter a value (e.g., 123, 3.14, hello, True): ")

    print("\n--- Displaying the value in different data types ---")

    # 2. Print as its original string type
    print(f"As a string (original input): '{user_input}' (Type: {type(user_input)})")

    # 3. Attempt to convert and print as an integer
    try:
        int_value = int(user_input)
        print(f"As an integer: {int_value} (Type: {type(int_value)})")
    except ValueError:
        print(f"As an integer: Cannot convert '{user_input}' to an integer.")

    # 4. Attempt to convert and print as a float
    try:
        float_value = float(user_input)
        print(f"As a float: {float_value} (Type: {type(float_value)})")
    except ValueError:
        print(f"As a float: Cannot convert '{user_input}' to a float.")

    # 5. Attempt to convert and print as a boolean
    # Python's bool() function converts empty strings, 0, and None to False.
    # Other non-empty strings and non-zero numbers convert to True.
    # For more specific boolean parsing (e.g., "True" -> True, "False" -> False),
    # you might need custom logic, but bool() is the built-in way.
    bool_value = bool(user_input)
    print(f"As a boolean: {bool_value} (Type: {type(bool_value)})")


if __name__ == "__main__":
    demonstrate_data_types()
