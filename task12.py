# Task 12: Salary Calculator 
# An employee receives a basic salary of ₹25,000. 
# Calculate: 
# • HRA = 20% of basic salary. 
# • DA = 10% of basic salary. 
# • Total salary = Basic salary + HRA + DA. 
# Display the salary details.

basic_salary = 25000

# Calculate HRA and DA
hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100

# Calculate total salary
total_salary = basic_salary + hra + da

print("Basic Salary: ₹", basic_salary)
print("HRA: ₹", hra)
print("DA: ₹", da)
print("Total Salary: ₹", total_salary)
