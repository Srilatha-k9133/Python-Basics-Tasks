#AREA OF SQUARE,RECTANGLE,CIRCLE

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
