###############################################################
# Scenario: Employee Performance Review

# Finding Maximum, Minimum, and Average Performance Scores 
# Without Built-in Functions
# YOU CANNOT USE ANY PYTHON INBUILT FUNCTIONS TO DO THIS.

# A company conducts annual performance reviews for employees. 
# Each employee is given a performance score out of 100. 
# The HR department wants to:

# - Identify the top-performing employee (highest score).
# - Identify the lowest-performing employee (lowest score).
# - Calculate the average performance score, rounded to 2 decimal places.
# - Identify underperforming employees (those with scores below 50) 
#    -> save them into another dictionary called non_performers.
#   and print a performance warning message to all of these employees.

performance_scores = {
    'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
    'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
    'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
    'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# write your code here
highest = performance_scores['Alice']
for name in performance_scores:
    if performance_scores[name] > highest:
        highest = performance_scores[name]
print(highest)

lowest = performance_scores['Alice']
for name in performance_scores:
    if performance_scores[name] < lowest:
        lowest = performance_scores[name]
print(lowest)

totalpoint = 0
count = 0
for name in performance_scores:
    totalpoint += performance_scores[name]
for number in performance_scores:
    count += 1

average = totalpoint/count
print(average)

non_performers = {}
for names in performance_scores:
    if performance_scores[names] < 50:
        non_performers[names] = performance_scores[names]
        ### add this name and score into non_performers
print(non_performers)
# dictionary[key] = value # to add and change
        