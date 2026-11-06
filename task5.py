# Task 5: Student Result 
# • Write a program to store a student's name and marks in three subjects. 
# • Calculate the total and average. 
# • Use proper indentation and comments. 

name = input("Enter student name: ")

marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculate total and average
total = marks1 + marks2 + marks3
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
