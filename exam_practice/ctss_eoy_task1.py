# Task 1

# The task is to edit program code that allows the user to enter and 
# edit the names and heights of team members.

# The following program allows the user to enter the names of the 
# 5 members of a team and stores them in a list. 

# The list is to be sorted and processed in each sub-task.
# This program allows the user to enter five names and
# stores the names in a list for further processing

# names = []

# for i in range(5):
#     name = input('Please enter the name: ')
#     names.append(name)

# print(names)

# Task 1.1
# Edit the program so that it:
# (a) creates a new list to store the collection of height data 
# for the corresponding names input.
# (b) allows the user to enter height data (in cm).
# (c) identifies the tallest and shortest height (not the person) 
#     among the entered data.
# Save your program.
# [4]
#--------------------------------------------


# names = []
# heights = []

# for i in range(5):
#     name = input('Please enter the name: ')
#     height = input("Please enter the height(in cm): ")
#     names.append(name)
#     heights.append(height)
# maxheight = max(heights)
# minheight = min(heights)

# print(names)
# print(f"The tallest height is {maxheight}")
# print(f"The shortest height is {minheight}")



#--------------------------------------------
# Task 1.2
# Copy and paste your program from sub-task 1.1.
# Edit the program to perform presence check and type check data 
# validation on the input for height data.
# Save your program.
# [3]
#--------------------------------------------

# names = []
# heights = []
# for i in range(5):
#     name = input('Please enter the name: ')
#     while True:
#         height = input("Please enter the height(in cm): ")
#         if height == "":
#             print("Please enter a value.")
#         elif not height.isdigit():
#             print("Please enter your height in numbers")
#         else:
#             break
#     names.append(name)
#     heights.append(height)
# maxheight = max(heights)
# minheight = min(heights)

# print(names)
# print(f"The tallest height is {maxheight}")
# print(f"The shortest height is {minheight}")





#--------------------------------------------
# Task 1.3
# Copy and paste your program from sub-task 1.2
# Edit the program so that it prints out:
# (a) the tallest and the shortest person from the entered data.
# (b) the average of the heights of the entered data.
# (c) the range of the heights data. ?? 
# Save your JupyterLab notebook for Task 1.
# [4]
#--------------------------------------------


names = []
heights = []

for i in range(5):
    name = input('Please enter the name: ')

    while True:
        height = input("Please enter the height(in cm): ")
        if height == "":
            print("Please enter a value.")
        elif not height.isdigit():
            print("Please enter your height in numbers")
        else:
            height = int(height)
            break

    names.append(name)
    heights.append(height)

# print(name)    
# print(heights)    

maxheight = max(heights)
minheight = min(heights)
shortest_pos = heights.index(minheight)
shortest_person = names[shortest_pos]
tallest_pos = heights.index(maxheight)
tallest_person = names[tallest_pos]

sum_height = sum(heights)
total_people = len(names)
average = sum_height / total_people

print(names)
print(f"The tallest height is {maxheight}")
print(f"The tallest person is {tallest_person}")
print(f"The shortest height is {minheight}")
print(f"The shortest person is {shortest_person}")
print(f"The average height is {average}")


