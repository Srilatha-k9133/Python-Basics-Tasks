# Task 10: Swap Two Variables 
# • Take two numbers as input. 
# • Swap their values without using a third variable.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping:")
print("num1 =", num1)
print("num2 =", num2)

# Swap values
num1, num2 = num2, num1

print("After swapping:")
print("num1 =", num1)
print("num2 =", num2)
