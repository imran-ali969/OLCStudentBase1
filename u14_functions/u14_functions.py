#def a function
def hello():
     print("hello world")

#call a functiom
# hello()

### def function with parameter
# def greet(you):
#      print(f"Hello {you}")

# # greet("name")
# def yourname(you, myname):
#      greet(you)
#      print(f"My name is {myname}")

# yourname("david", "ali")


list_radius = [8.85, 63.8, 9.6, 9.4, 2.1, 5.8, 1.5, 8.4, 63.8]
total_area = 0
def area(radius):
     area_circle = 3.1514 * radius ** 2

     return area_circle

# find the total area of all the circles in the list
# for i in list_radius:

#     #  total = area(i) 
#      total_area += total

# print(total)






# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.
def calc(num1, num2, operator):

     # check the operator to decide what to do
     if operator == "+":
          result = num1 + num2
          # print(result)
     elif operator == "-":
          result = num1 - num2
          # print(result2)
     elif operator == "*":
          result = num1 * num2
     elif operator == "/":
          result = num1 / num2
          #....

     return result
     
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
op = input("Enter an operation + - * / : ")
cal_result = calc(num1, num2, op)
print(cal_result)


# Test the function with multiple operations.





