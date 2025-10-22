"""
write a program to enter a number and display it evuavalent hexa and octal number also print square root of number
"""
import math

def number_operations():
    """
    Prompts the user to enter a number and displays its hexadecimal,
    octal, and square root equivalents.
    """
    try:
        # 1. Get input from the user
        num_str = input("Enter an integer number: ")
        number = int(num_str)

        # 2. Calculate hexadecimal and octal equivalents
        hexa_equivalent = hex(number)
        octal_equivalent = oct(number)

        # 3. Display the results
        print("\n--- Results ---")
        print(f"The number you entered: {number}")
        print(f"Hexadecimal equivalent: {hexa_equivalent}")
        print(f"Octal equivalent: {octal_equivalent}")

        # 4. Calculate and display the square root, handling negative numbers
        if number < 0:
            print("Square root: Not defined for a negative number.")
        else:
            square_root = math.sqrt(number)
            print(f"Square root: {square_root:.4f}") # Formatted to 4 decimal places

    except ValueError:
        # Handle cases where the input is not a valid integer
        print(f"Error: Invalid input '{num_str}'. Please enter a valid integer.")

if __name__ == "__main__":
    number_operations()