# Task 3
# The task is to edit program code so that countries and their capital 
# cities can be added to or removed from a dictionary.

# The following program has a dictionary that contains countries 
# and their capital cities. The program allows the user to:

# • input a country
# • input whether they want to remove a country and 
#    its capital city from the dictionary
# • input whether they want to add a country and its 
#    capital city to the dictionary.


# capital_cities = {
#     'singapore':'Singapore',
#     'japan':'Tokyo', 
#     'australia':'Canberra',
#     'england':'London',
#     'france':'Paris',
#     'germany':'Berlin'
# }

# country = input("Please enter the name of a country: ")
# country = country.lower()

# if country in capital_cities:
#     capital = capital_cities[country]
#     print(f"The capital of {country} is {capital}")

# for i in capital_cities:
#     print(f"The capital of {country} is {capital_cities[i]}")

# For all sub-tasks, you can assume that all user input is valid.
#  All countries input to be searched or removed are found in the dictionary.

# Task 3.1
# Edit the program so that it:
# • converts the input for country to lower case
# • searches the dictionary for the country input and outputs the capital city of that country.
# Save your program.    [3]


#####################################

# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 99}

# Task 1: Identify and print the name and score of the highest scoring student.
# highest_score = 0
# highest_student = ""
# for i in students:
#     if students[i] > highest_score:
#         highest_score= students[i]
#         highest_student = i

# print(highest_score)
# print(highest_student)

#------------------------------------------------------------
# Task 2: Calculate and display the name and score of students scoring above 80.

students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 72}
# for e in students:
#     if students[e] > 80:
#         print(f"{e} scored {students[e]}")



#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.
for s in students:
    students[s] = students[s] + 5
print(students)


# students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 72}
# students["Alice"] = students["Alice"] + 5