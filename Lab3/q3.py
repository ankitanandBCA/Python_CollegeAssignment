"""
Demonstrates common list operations: indexing, slicing, append, pop, remove, reverse, and sort.
"""

# Initial list of programming languages
languages = ["Python", "Java", "C++", "JavaScript", "Go"]
print(f"Initial list: {languages}\n")






# 1. Indexing: Accessing elements by their position
print("--- 1. Indexing ---")
print(f"Element at index 0: {languages[0]}")  # First element
print(f"Element at index 2: {languages[2]}")
print(f"Last element (using -1): {languages[-1]}")  # Last element
print("-" * 20 + "\n")







# 2. Slicing: Getting a sub-list
print("--- 2. Slicing ---")
print(f"Slice from index 1 to 3 (exclusive): {languages[1:3]}")
print(f"Slice from the beginning to index 2 (exclusive): {languages[:2]}")
print(f"Slice from index 2 to the end: {languages[2:]}")
print(f"A copy of the whole list: {languages[:]}")
print("-" * 20 + "\n")






# 3. append(): Adding an element to the end of the list
print("--- 3. append() ---")
print(f"List before append: {languages}")
languages.append("Rust")
print(f"List after appending 'Rust': {languages}")
print("-" * 20 + "\n")






# 4. pop(): Removing an element by its index (or the last one if no index is given)
print("--- 4. pop() ---")
print(f"List before pop: {languages}")
removed_element = languages.pop()  # Removes the last element, "Rust"
print(f"Popped element (last one): {removed_element}")
print(f"List after popping last element: {languages}")
removed_element_by_index = languages.pop(1)  # Removes element at index 1, "Java"
print(f"Popped element at index 1: {removed_element_by_index}")
print(f"List after popping element at index 1: {languages}")
print("-" * 20 + "\n")






# 5. remove(): Removing the first occurrence of a specific value
print("--- 5. remove() ---")
# Let's add a duplicate to show it only removes the first one
languages.append("C++")
print(f"List before remove (with duplicate 'C++'): {languages}")
languages.remove("C++")
print(f"List after removing 'C++': {languages}")
print("-" * 20 + "\n")








# 6. reverse(): Reversing the order of elements in-place
print("--- 6. reverse() ---")
print(f"List before reverse: {languages}")
languages.reverse()
print(f"List after reverse: {languages}")
print("-" * 20 + "\n")








# 7. sort(): Sorting the elements in-place
print("--- 7. sort() ---")
# Note: 'short' in the prompt is interpreted as 'sort'
print(f"List before sort: {languages}")
languages.sort()  # Sorts alphabetically (ascending)
print(f"List after sort (ascending): {languages}")
languages.sort(reverse=True)  # Sorts in descending order
print(f"List after sort (descending): {languages}")
print("-" * 20 + "\n")