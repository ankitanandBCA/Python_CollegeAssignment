"""
implement nested if and loop based logic for pattern genaraction program
"""

print("--- Program 1: Hollow Rectangle Pattern ---")
rows = 5
cols = 7

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for columns
    for j in range(1, cols + 1):
      
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() # Move to the next line after each row

# --- Program 2: Right-Angled Triangle with Alternating Characters ---

print("\n--- Program 2: Right-Angled Triangle with Alternating Characters ---")
size = 5

# Outer loop for rows
for i in range(1, size + 1):
   
    for j in range(1, i + 1):
     
        if j % 2 == 1:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print() # Move to the next line after each row

# --- Program 3: Number Pyramid with Conditional Display ---

print("\n--- Program 3: Number Pyramid with Conditional Display ---")
height = 5


for i in range(1, height + 1):
    
    for _ in range(height - i):
        print(" ", end=" ")
    

    for j in range(1, 2 * i):

        if j % 2 == 1:
          
            if j == 1 or j == (2 * i - 1):
                print(i, end=" ")
            else:
               
                print(j, end=" ")
        else:
          
            print("-", end=" ")
    print() 