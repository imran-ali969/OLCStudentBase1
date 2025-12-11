# 
# print("aaaa")
# for i in range(3):
#     print("bbbb")
# print("cccc")

# for i in range(2):
#     print("Mary had a")
    
#     for j in range(3):
#         print("little lamb")

# print("whose fleece was white as snow")



# Mary had a 
# little lamb
# little lamb
# little lamb

# Mary had a 
# little lamb
# little lamb
# little lamb

# whose fleece was white as snow




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Printing Odd Numbers
# Write a program to print all odd numbers from 1 to 15.
# Use range(start, stop, step) to skip even numbers.
# Example: Output = 1, 3, 5, ..., 15.



#------------------------------------------------------------
# Exercise 9: Multiplying Numbers
# Write a program to print the first 5 multiples of 7.
# Use range(start, stop, step).
# Example: Output = 7, 14, 21, 28, 35.
# for i in range(7,36,7):
#     print(i)

#------------------------------------------------------------
# Exercise 10: Repeating a Phrase
# Write a program to print "I love Python!" 3 times.
# Use range(stop) to repeat the phrase.
# for i in range(3):
#     print("I love Python!")


#------------------------------------------------------------
# Exercise 11: Custom Counting Pattern
# Write a program to print the following pattern:
# 5
# 44
# 333
# 2222
# 11111

# print("5" * 1)
# print("4" * 2)
# print("3" * 3)
# print("2" * 4)
# print("1" * 5)
# count = 1
# for i in range(5,0,-1):
#     # print(f"{str(i)}" * f"{count}")
#     print(f"{str(i)* count}")
#     count += 1



#------------------------------------------------------------
# Exercise 13: Printing a Custom Star Pattern
# Write a program to print the following pattern:
# *
# ***
# *****
# *******
# *********
# count = ("*")
# for i in range(1,10,2):
#     print(f({}))
# number = input("what number do you want: ")
# for i in range(1,13):
#     print(f"{number} x {i} =" f"{int(number) * i}")

# random >>> generate a random number
import random # happens once at the top of program

# random.randint(startnumber, endnumber)
# rannum = random.randint(1, 6) # return you a random number
# print(rannum)
# num1 = int(input("pick your first number: "))
# num2 = int(input("pick your second number: "))
# if num1 > num2:
#     print("num1 is bigger than num2")
# elif num1 < num2:
#     print("num1 is smaller than num2")
# else:
#     print("num1 is equal to num2")

# ask 10 questions, for every correct, score + 1, at end, say how many correct
# import random
# correct = 0
# for i in range(10):
#     num1 = random.randint(10,30)
#     num2 = random.randint(10,30)
#     answer = int(input(f"What is {num1} + {num2}: "))
#     if answer == num1 + num2:
#         print("correct answer")
#         correct += 1
#     else:
#         print("incorrect answer")
#         correct -= 1

# print(f"you got {correct} answers")

pens = int(input("How many pens do you want: "))
cost = 5
total_cost = pens * cost
discounted = 0
if pens >= 100:
    discounted = total_cost * 0.10
    print(f"Your final amount is ${discounted} for {pens} pens. Pls pay ${total_cost - discounted}")
else:
    print(f"Your final amount is ${total_cost} for {pens} pens.")




