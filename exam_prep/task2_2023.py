### The below are the starter codes provided for 
### the questions on Refinement of Program
### Copy and Paste this as part of the start of Your Question.

######### ANIMALGAME.py #########
# Task 1.1
#---------------------------------    
######### ANIMALGAME.py #########
# 4 marks
p1_list = []
while True:
    p1_animal= input("Player 1, please enter an animal: ")
    p1_animal = p1_animal.lower()
    p1_list.append(p1_animal)
    proceed = input("Do you wish to add another animal y/n: ")
    if proceed.lower() == "y":
        continue
    else:
        break
p2_guess = input("Player 2, please enter your guess: ")
p2_guess = p2_guess.lower()
# print(p1_list) # testing
  



# Task 1.2
#---------------------------------
# 4 marks
p2_score = 0 
p1_list = []
while True:
    p1_animal= input("Player 1, please enter an animal: ")
    p1_animal = p1_animal.lower()
    p1_list.append(p1_animal)
    proceed = input("Do you wish to add another animal y/n: ")
    if proceed.lower() != "y":
        break
p2_guess = input("Player 2, please enter your guess: ")
p2_guess = p2_guess.lower()
print(p1_list)
if p2_guess in p1_list:
    p1_list.remove(p2_guess)
    p2_score += 1
print(p2_score)



# Task 1.3
#---------------------------------
# 3 marks
p2_score = 0 
p1_list = []
while True:
    p1_animal= input("Player 1, please enter an animal: ")
    p1_animal = p1_animal.lower()
    p1_list.append(p1_animal)
    proceed = input("Do you wish to add another animal y/n: ")
    if proceed.lower() != "y":
        break
while True:
    p2_guess = input("Player 2, please enter your guess: ")
    p2_guess = p2_guess.lower()
    if p2_guess in p1_list:
        p1_list.remove(p2_guess)
        p2_score += 1
    else:
        print("Game over")
        print(f"{p1_list} were not guess")
        print(f"Your score is {p2_score}")
        break
    if len(p1_list) == 0:
        print("All animals were guessed correctly")
        print(f"Your score is {p2_score}")
        break

    