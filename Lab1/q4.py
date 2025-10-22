"""
write a program if-else and if-elif-else condition for decision macking
"""


print("--- Part 1: Even or Odd Checker (if-else) ---")
try:
    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        print(f"The number {number} is Even.")
  
    else:
        print(f"The number {number} is Odd.")

except ValueError:
    print("Invalid input. Please enter a whole number (integer).")


print("\n--- Part 2: Simple Grading System (if-elif-else) ---")
try:
    score = float(input("Enter your score (0-100): "))

   
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
   
    else:
        grade = "F"

  
    if 0 <= score <= 100:
        print(f"With a score of {score}, your grade is: {grade}")
    else:
        print("Score must be between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter a numerical score.")


print("\n--- Part 3: Day of the Week (if-elif-else) ---")
day_number = 3
if day_number == 1:
    print("It's Monday.")
elif day_number == 2:
    print("It's Tuesday.")
elif day_number == 3:
    print("It's Wednesday.")
else:
    print("It's another day or an invalid day number.")