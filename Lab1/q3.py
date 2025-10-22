"""
create input and output based calcuting using different operator and these presdicent

"""

print("--- Enter two numbers for basic calculations ---")
try:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
 
    exit()


print("\n--- Basic Arithmetic Operations ---")
print(f"Addition:        {num1} + {num2} = {num1 + num2}")
print(f"Subtraction:     {num1} - {num2} = {num1 - num2}")
print(f"Multiplication:  {num1} * {num2} = {num1 * num2}")
print(f"Exponentiation:  {num1} ** {num2} = {num1 ** num2}")


if num2 != 0:
    print(f"Division:        {num1} / {num2} = {num1 / num2}")
    print(f"Floor Division:  {num1} // {num2} = {num1 // num2} (integer part of division)")
    print(f"Modulo:          {num1} % {num2} = {num1 % num2} (remainder of division)")
else:
    print("\nCannot perform Division, Floor Division, or Modulo because the second number is zero.")



print("\n--- Operator Precedence Demonstration ---")
a, b, c = 10, 5, 2
print(f"Using numbers a={a}, b={b}, c={c}")



result1 = a + b * c
print(f"Expression: a + b * c  =>  {a} + {b} * {c}")
print(f"Result: {result1}  (Note: {b}*{c} is calculated first, then added to {a})")


result2 = (a + b) * c
print(f"\nExpression: (a + b) * c  =>  ({a} + {b}) * {c}")
print(f"Result: {result2} (Note: ({a}+{b}) is calculated first due to parentheses)")
