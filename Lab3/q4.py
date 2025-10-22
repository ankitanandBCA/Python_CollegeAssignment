"""
use list comprechesion to create new list form existing 1.
"""

# An existing list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}\n")





# ==============================================================================
# Example 1: Create a new list with each number squared.
# ==============================================================================
# Syntax: [expression for item in iterable]

print("1. Creating a new list of squares:")
squares = [x**2 for x in numbers]
print(f"   New list of squares: {squares}\n")





# ==============================================================================
# Example 2: Create a new list with only the even numbers.
# ==============================================================================
# Syntax: [expression for item in iterable if condition]

print("2. Creating a new list of only even numbers:")
evens = [x for x in numbers if x % 2 == 0]
print(f"   New list of evens: {evens}\n")






# ==============================================================================
# Example 3: Create a new list of squares for only the even numbers.
# ==============================================================================
# Here we combine the transformation and the condition.

print("3. Creating a new list of squares of even numbers:")
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"   New list of even squares: {even_squares}\n")






# ==============================================================================
# For comparison, here is how Example 3 would be written with a for-loop.
# List comprehensions are more "Pythonic" and concise.
# ==============================================================================
print("4. Doing the same thing with a traditional for-loop:")
even_squares_loop = []
for x in numbers:
    if x % 2 == 0:
        even_squares_loop.append(x**2)
print(f"   Result from for-loop: {even_squares_loop}")
print("   --> The result is identical, but the list comprehension is shorter.")