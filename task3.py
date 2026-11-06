# Task 3: Area Calculator 
# • Write a program to calculate the area of a rectangle, square, and circle. 
# • Take the required values as input.

length = float(input("Enter a length of rectangle:"))
width = float(input("Enter a width of rectangle:"))
rectangle_area=length * width

side = float(input("Enter a side of square:"))
square_area=side*side

radius = float(input("Enter a radius of circle:"))
circle_area=3.14*radius**2

print("Area of rectangle:",rectangle_area)
print("Area of square:",square_area)
print("Area of circle:",circle_area)
