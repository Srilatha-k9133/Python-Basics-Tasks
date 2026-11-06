# Task 8: Keyword Identification 
# • Write a program to display all Python keywords using the keyword module. 
# • Explain any five keywords with examples.

import keyword

print("Python Keywords:")
print(keyword.kwlist)


#Five keywords explained
1. if – Used to check a condition.
age = 20
if age >= 18:    
  print("Eligible")


2. else – Executes when the if condition is false.
age = 16
if age >= 18:    
  print("Eligible")
else:   
  print("Not Eligible")


3. for – Used for looping.
for i in range(5):   
  print(i)


4. def – Used to create a function.
def greet():   
  print("Hello")greet()


5. return – Used to return a value from a function.
def add(a, b):
  return a + bprint(add(10, 20))

