"""
write a program to calculate distance between two points
"""
import math

def calculate_distance():
    """
    Calculates the Euclidean distance between two points (x1, y1) and (x2, y2) in a 2D plane.
    """
    print("--- Distance Calculator Between Two Points ---")

    try:
        # 1. Get coordinates for the first point from the user
        print("\nEnter coordinates for the first point:")
        x1_str = input("  Enter x-coordinate (x1): ")
        y1_str = input("  Enter y-coordinate (y1): ")

        # 2. Get coordinates for the second point from the user
        print("\nEnter coordinates for the second point:")
        x2_str = input("  Enter x-coordinate (x2): ")
        y2_str = input("  Enter y-coordinate (y2): ")

        # 3. Convert all inputs to floating-point numbers
        x1 = float(x1_str)
        y1 = float(y1_str)
        x2 = float(x2_str)
        y2 = float(y2_str)

        # 4. Calculate the distance using the distance formula
        # d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        print("\n--- Result ---")
        print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.4f}")

    except ValueError:
        print("\nError: Invalid input. Please enter valid numbers for all coordinates.")

if __name__ == "__main__":
    calculate_distance()
