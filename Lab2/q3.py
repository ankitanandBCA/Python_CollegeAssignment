"""
write a program to calculate area of trangle using herons formula
"""
import math

def calculate_herons_area():
    """
    Calculates the area of a triangle using Heron's formula based on user input for the side lengths.
    It includes validation to ensure the sides can form a valid triangle.
    """
    print("--- Triangle Area Calculator (Heron's Formula) ---")

    try:
        # 1. Get the lengths of the three sides from the user
        a_str = input("Enter the length of the first side (a): ")
        b_str = input("Enter the length of the second side (b): ")
        c_str = input("Enter the length of the third side (c): ")

        # Convert inputs to floating-point numbers
        a = float(a_str)
        b = float(b_str)
        c = float(c_str)

        # 2. Validate if the sides can form a triangle (Triangle Inequality Theorem)
        if (a + b > c) and (a + c > b) and (b + c > a):
            # 3. Calculate the semi-perimeter (s)
            s = (a + b + c) / 2

            # 4. Calculate the area using Heron's formula
            # The term inside the sqrt is s * (s - a) * (s - b) * (s - c)
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))

            print("\n--- Result ---")
            print(f"The area of the triangle is: {area:.4f}")
        else:
            print("\nError: The provided side lengths cannot form a valid triangle.")
            print("The sum of any two sides must be greater than the third side.")

    except ValueError:
        print("\nError: Invalid input. Please enter valid numbers for the side lengths.")

if __name__ == "__main__":
    calculate_herons_area()