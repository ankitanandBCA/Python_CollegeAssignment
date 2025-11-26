
students_list = []


print("Enter the name and marks for 5 students:")
for i in range(5):
    print(f"\n--- Student {i + 1} ---")
    name = input("Enter name: ")
    
   
    while True:
        try:
            marks = int(input("Enter marks: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value for marks.")
            
   
    student_dict = {'name': name, 'marks': marks}
 
    students_list.append(student_dict)


print("\n--- Student Grades ---")
for student in students_list:
    if student['marks'] > 90:
        print(f"{student['name']} has Grade 'A'")
    elif 80 < student['marks'] <= 90:
        print(f"{student['name']} has Grade 'B'")
    elif 70 < student['marks'] <= 80:
        print(f"{student['name']} has Grade 'C'")
    elif 60 < student['marks'] <= 70:
        print(f"{student['name']} has Grade 'D'")
    else:
        print(f"{student['name']} has Grade 'F'")




