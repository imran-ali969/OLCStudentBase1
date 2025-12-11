# Task 4
# The task is to write a program that computes the aggregate score of all the 
# subject grade points achieved by the students in an examination.
# The final examination score for every subject taken by a student is 
# classified according to the following grading system:

# All codes should have appropriate comments and all identifiers should be appropriately
# named. [2]

# Task 4.1
# Write a function getgradepoint ( ) that has a parameter mark passed to it. The
# function must return the grade point for the mark based on the grading system. [4]
# Grade	Marks	Grade Point
# A1	    75-100	1
# A2	    70-74	2
# B3	    65-69	3
# B4	    60-64	4
# C5	    55-59	5
# C6	    50-54	6
# D7	    45-49	7
# E8	    40-44	8
# F9	    0-39	9
#------------------------------------------------------------
def getgradepoint(result):
    grade = 0
    if result >= 75 and result<=100:
        grade = 1
    elif result >=70 and result<= 74:
        grade = 2
    elif result >=65 and result<= 69:
        grade = 3
    elif result >=60 and result<= 64:
        grade = 4
    elif result >=55 and result<= 59:
        grade = 5
    elif result >=50 and result<= 54:
        grade = 6
    elif result >=45 and result<= 49:
        grade = 7
    elif result >=40 and result<= 44:
        grade= 8
    elif result <=39:
        grade = 9
    # print(grade)
    return grade  

    


# result = int(input("Enter your result: "))
test1 = getgradepoint(76)
print(test1)

# Task 4.2
# Write a function calL1R5( ) that takes the result as a parameter. 
# result is a dictionary with the key being the subject, and the value being the score. 
# Here is a sample dictionary format:
# {"English":71, "Higher Chinese":71, "Chemistry":71, "Geography":71, 
#  "Mathematics":71, "Physics":71,"Computing":71}


# Your function needs to
# • either compute English or Higher Chinese as a L1 subject, whichever grade
# point is lower
# • compute the remaining subjects as the R5 subjects
# • add the grade points of the L1 and R5 subjects as the L1 R5 score [3]
#------------------------------------------------------------
def call1r5(result):
    english = result["English"]
    hchinese = result["Higher Chinese"]

    l1 = 0
    if english > hchinese:
        l1 = getgradepoint(english)
    else:
        l1 = getgradepoint(hchinese)
    r5 = 0
    for subject in result:
        if subject == "English" or subject == "Higher Chinese":
            continue
        else:
            score = result[subject]
            r5 = r5 + getgradepoint(score)
    return l1 + r5




test = {"English":71, "Higher Chinese":80, "Chemistry":70, "Mathematics":60, "Physics":66, "Computing":80, "Geography":72} 
print(call1r5(test))

# Task 4.3
# Your main program should use the calL1R5( ) function and display the L1R5
# aggregate score.						[2]
# Test your program with the following input:
# Subjects	Marks
# English	71istry":63, "Geography":72, "Mathematics":60, "Physics":66,"Computi
# Higher Chinese	80
# Chemistry	63
# Geography	72
# Mathematics	60
# Physics	66
# Computing	70
#------------------------------------------------------------

result = {"English":0, "Higher Chinese":0, "Chemistry":0, "Geography":0, "Mathematics":0, "Physics":0,"Computing":0} 

for subject in result:
    current_score = int(input(f"What is the score for {subject}: "))
    result[subject] = current_score

calculated_l1r5 = call1r5(result)

print(f"Your L1R5 is {calculated_l1r5}")

