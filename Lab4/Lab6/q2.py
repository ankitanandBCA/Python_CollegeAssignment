
print("Enter 5 names for the first tuple:")
names1 = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names1.append(name)
tuple1 = tuple(names1)


print("\nEnter 5 names for the second tuple:")
names2 = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names2.append(name)
tuple2 = tuple(names2)


set1 = set(tuple1)
set2 = set(tuple2)


common_names = set1.intersection(set2)


if common_names:
    print(f"\nThe common names are: {list(common_names)}")
else:
    print("\nThere are no common names between the two tuples.")
