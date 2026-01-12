# 1. Create a dictionary with 5 students and their marks.
students = {
    "Aarav": 85,
    "Vivaan": 92,
    "Diya": 78,
    "Ishaan": 95,
    "Ananya": 88
}
print(f"1. Initial Dictionary: {students}")

# 2. Print the value of a specific student using their name as key.
print(f"2. Vivaan's Marks: {students['Vivaan']}")

# 3. Add a new student with marks to the dictionary.
students["Rohan"] = 82
print(f"3. After adding Rohan: {students}")

# 4. Update the marks of an existing student.
students["Aarav"] = 90
print(f"4. After updating Aarav's marks: {students}")

# 5. Delete a student from the dictionary.
del students["Diya"]
print(f"5. After deleting Diya: {students}")

# 6. Print all student names using keys().
print(f"6. Student Names: {list(students.keys())}")

# 7. Print all student marks using values().
print(f"7. Student Marks: {list(students.values())}")

# 8. Print all student names with their marks using items().
print("8. Items:")
for name, marks in students.items():
    print(f"   - {name}: {marks}")

# 9. Check if a specific student is in the dictionary.
is_present = "Ishaan" in students
print(f"9. Is Ishaan in the dictionary? {is_present}")

# 10. Check if a specific mark is present in the dictionary values.
mark_present = 95 in students.values()
print(f"10. Is mark 95 present? {mark_present}")

# 11. Use get() to fetch a student's marks safely.
# If 'Suresh' doesn't exist, it returns 'Not Found'
grade = students.get("Suresh", "Not Found")
print(f"11. Fetching Suresh's marks (safe): {grade}")

print("\n--- Part 2: Employee Dictionary & Sorting ---")

# 12. Create a dictionary of employees with their departments.
employees = {
    "Rajesh": "HR",
    "Priya": "IT",
    "Amit": "Finance",
    "Sneha": "IT",
    "Vikram": "Marketing"
}
print(f"12. Employee Dictionary: {employees}")

# 13. Access the department of a specific employee.
print(f"13. Priya's Department: {employees['Priya']}")

# 14. Add a new employee and department.
employees["Meera"] = "Sales"
print(f"14. After adding Meera: {employees}")

# 15. Change the department of an existing employee.
employees["Rajesh"] = "Operations"
print(f"15. After changing Rajesh's department: {employees}")

# 16. Remove an employee from the dictionary.
removed_val = employees.pop("Amit")
print(f"16. After removing Amit (who was in {removed_val}): {employees}")

# 17. Sort the employee dictionary by employee names (keys) in ascending order.
sorted_by_name = dict(sorted(employees.items()))
print(f"17. Sorted by Name (Asc): {sorted_by_name}")

# 18. Sort the employee dictionary by department names (values) in ascending order.
sorted_by_dept = dict(sorted(employees.items(), key=lambda item: item[1]))
print(f"18. Sorted by Dept (Asc): {sorted_by_dept}")

# 19. Sort the employee dictionary by names in descending order.
sorted_by_name_desc = dict(sorted(employees.items(), reverse=True))
print(f"19. Sorted by Name (Desc): {sorted_by_name_desc}")

# 20. Sort the employee dictionary by department in descending order.
sorted_by_dept_desc = dict(sorted(employees.items(), key=lambda item: item[1], reverse=True))
print(f"20. Sorted by Dept (Desc): {sorted_by_dept_desc}")

print("\n--- Part 3: Advanced Operations ---")

# 21. Find all keys that have a specific value in a dictionary.
# Let's find all employees in 'IT' from the previous list
target_dept = "IT"
it_employees = [k for k, v in employees.items() if v == target_dept]
print(f"21. Employees in {target_dept}: {it_employees}")

# 22. Count how many students scored above 80 marks.
# Using the 'students' dict from Part 1
count_above_80 = sum(1 for mark in students.values() if mark > 80)
print(f"22. Students scoring > 80: {count_above_80}")

# 23. Create a nested dictionary for 3 students with age, grade, and department.
student_details = {
    "Arjun": {"age": 20, "grade": "A", "dept": "CS"},
    "Zara": {"age": 21, "grade": "B", "dept": "Math"},
    "Kabir": {"age": 19, "grade": "A", "dept": "Physics"}
}
print(f"23. Nested Dictionary created.")

# 24. Access the grade of a student from the nested dictionary.
arjun_grade = student_details["Arjun"]["grade"]
print(f"24. Arjun's Grade: {arjun_grade}")

# 25. Update the department of a student in the nested dictionary.
student_details["Zara"]["dept"] = "Statistics"
print(f"25. Updated Zara's dept: {student_details['Zara']}")

# 26. Loop through the nested dictionary and print student names with their grades.
print("26. Student Grades:")
for std, details in student_details.items():
    print(f"    - {std}: {details['grade']}")

# 27. Merge two dictionaries of students into one.
group_A = {"Neha": 85, "Rahul": 90}
group_B = {"Pooja": 78, "Vikas": 92}
# Using the union operator '|' (Python 3.9+) or .update()
merged_group = group_A | group_B 
print(f"27. Merged Dictionary: {merged_group}")

# 28. Clear all entries in a dictionary.
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(f"28. Cleared Dictionary: {temp_dict}")

# 29. Copy a dictionary into a new dictionary and modify the copy.
original = {"x": 10, "y": 20}
copy_dict = original.copy()
copy_dict["x"] = 99
print(f"29. Original: {original}, Copy (modified): {copy_dict}")

# 30. Create a dictionary where keys are numbers 1-5 and values are their squares.
squares = {x: x**2 for x in range(1, 6)}
print(f"30. Squares Dictionary: {squares}")