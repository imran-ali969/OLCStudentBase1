# using for loop

# print numbers from 5 - 10

# print multiples of 7 from 7 to 84

# count down from 10 to 1

# for i in range(5,11,1):
#     print(i)

# for i in range(7,85,7):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

import random

number = random.randint(1,100)
print(number)

for i in range(7):

    guess = int(input("Enter your guess: "))

    if guess > number:
        print("Your guess was too large")

    elif guess < number:
        print("Your guess was too small")

    else:
        print("Your guess was correct")
        break

else:
    print(f"you did not guess it, the correct answer was {number}")