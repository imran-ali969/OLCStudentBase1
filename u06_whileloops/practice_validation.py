# NRIC Validation

# - Validate that the first character is an alphabet
# - Validate that the last character is an alphabet
# - Validate that the middle 7 characters are numbers
# - Validate that total length must be 9
# while True:
#     nric = input("Enter your NRIC: ")
#     if not nric[0].isalpha():
#         print("Please make the first digit an aplhabet")
#     elif not nric[-1].isalpha():
#         print("Please make the last digit an alphabet")
#     elif not nric[1:8:1].isdigit():
#         print("Middle 7 digits must be numbers")
#     elif not len(nric) == 9:
#         print("Must have nine digits")
#     else:
#         print("Your NRIC is valid")
#         break
