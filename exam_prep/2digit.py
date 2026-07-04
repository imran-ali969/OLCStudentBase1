import random
secret_code = ""
for i in range(3):
    digit = str(random.randint(1, 5))
    secret_code = secret_code + digit

print("Guess the 3-digit number. Each digit is from 1 to 5: ")
print("You have 5 tries. Enter your guess (e.g. 123). ")
      