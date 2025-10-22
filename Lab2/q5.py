"""
write a program to demonstrate the use of relational operation
"""

def demonstrate_relational_operators():
    """
    Takes two numbers from the user and demonstrates the use of all
    relational operators by comparing them.
    """
    print("--- Relational Operator Demonstration ---")
    print("This program will compare two numbers you enter.\n")

    try:
        # 1. Get two numbers from the user
        a_str = input("Enter the first number (a): ")
        b_str = input("Enter the second number (b): ")

        # Convert inputs to floating-point numbers
        a = float(a_str)
        b = float(b_str)

        print("\n--- Results ---")
        print(f"Comparing a = {a} and b = {b}\n")

        # 2. Demonstrate each relational operator
        print(f"Is a > b?  ({a} > {b}):  {a > b}")
        print(f"Is a < b?  ({a} < {b}):  {a < b}")
        print(f"Is a == b? ({a} == {b}): {a == b}")
        print(f"Is a != b? ({a} != {b}): {a != b}")
        print(f"Is a >= b? ({a} >= {b}): {a >= b}")
        print(f"Is a <= b? ({a} <= {b}): {a <= b}")

    except ValueError:
        print("\nError: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    demonstrate_relational_operators()