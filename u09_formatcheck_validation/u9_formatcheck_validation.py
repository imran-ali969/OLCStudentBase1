# num =3.14523
# print(round(num, 2))
# import math
# print(math.ceil(num))

# validate for Valid nric
# 1st character must be alphabet
# last character also alphabet
# middle 7 must be number
# total length must be 9 character

#### WORKING CODE AND IT WORKS!
# while True:
#     nric = input("Enter your NRIC: ")
#     nric1 = nric[0]
#     nric2 = nric[-1]
#     nric3 = nric[1:8:1]
#     nric4 = len(nric)
#     if not nric1.isalpha():
#         print("Your first digit should be a letter")
#     elif not nric2.isalpha():
#         print("Your last digit should be a letter")
#     elif not nric3.isdigit():
#         print("Middle 7 numbers must be numbers")
#     elif not nric4 == 9:
#         print("You need 9  digits")
#     else:
#         print("Your  NRIC is valid")
#         break


###################################################
''' MULTI LINE STRING
Question 1 (Length Check):
Write the input entry and validation code for a program that
needs to accept a 4-digit OTP (One-Time Password)
The OTP must be exactly 4 digits long and must be numbers

If the input is invalid, your code should keep trying
by asking for the input to be entered again.

#########################################
'''
######### CODE BELOW WORKS
# while True:
#     otp = input("Enter your otp: ")
#     if len(otp) > 4 or len(otp) < 4:
#         print("otp must be 4 digits")
#     elif not otp.isdigit():
#         print("otp must be all numbers")
#     else:
#         print("otp is valid")
#         break




##################################################
# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# - At least one uppercase letter.
# - At least one lowercase letter.
# - At least one digit.
# - At least one special character !@#$%^&*

# Example:
# Input: "Secure123"
# Output: "Valid password"

# Input: "password"
# Output: "Invalid password"

## Bonus: Print out which of the requirement failed.
# while True:
#     hasupper = False
#     haslower = False
#     hasdigit = False
#     hasspecial = False
#     password = input("Enter your passwor: ")
#     for i in password:
#         if i.isupper():
#             hasupper = True
#         if i.islower():
#             haslower =True
#         if i.isdigit():
#             hasdigit = True
#         if i in "!@#$%^&*":
#             hasspecial =True
#     if len(password) < 8:
#         print("Password must be atleast 8 digit")
#     elif hasdigit == False:
#         print("Need atleast one number")
#     elif haslower == False:
#         print("Need atleast one lowercase letter")
#     elif hasupper == False:
#         print("Need atleast one uppercase letter")
#     elif hasspecial == False:
#         print("Need atleast one special character")
#     else:
#         print("Your password is valid")
#         break

print(ord("A"))
print(chr(65))


