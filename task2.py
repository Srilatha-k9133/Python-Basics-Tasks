# Task 2: Simple Calculator 
# • Write a program to perform addition, subtraction, multiplication, and division on two 
# numbers. 
# • Display the result of each operation. 

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

print("addition: ", a+b)
print("subtraction: ",a-b)
print("multiplication: ",a*b)
if b!=0:
  print("division: ",a/b)
else:
  print("not divisible by zero")
