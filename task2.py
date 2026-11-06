#Simple calculator
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

print("addition: ", a+b)
print("subtraction: ",a-b)
print("multiplication: ",a*b)
if b!=0:
  print("division: ",a/b)
else:
  print("not divisible by zero")
