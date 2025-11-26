import numpy as np

char_array = np.array(['a', 'b', 'c', 'd'], dtype='S1')
print("--- Character Array ---")
print(char_array)
print(f"Data type: {char_array.dtype}\n")


int_array = np.array([10, 20, 30, 40, 50])
print("--- Integer Array ---")
print(int_array)
print(f"Data type: {int_array.dtype}\n")


float_array = np.array([1.5, 2.7, 3.1, 4.9, 5.2])
print("--- Float Array ---")
print(float_array)
print(f"Data type: {float_array.dtype}\n")
