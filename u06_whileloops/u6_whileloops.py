# must be a valid number
# must be valid number between 1 to 100


while True:
    age = input("Enter your age: ")
    if not age.isdigit():
        print("Please enter a number")
    elif int(age) > 100 or int(age) < 0:
        print("Please enter a valid age")
    else:
        print(f"Your age is {age}")
        break

if int(age) < 7:
    print("Pre school")
elif int(age) <= 12:
    print("Primary school")
elif int(age) <= 16:
    print("Secondary school")
elif int(age) <= 18:
    print("Jc")
else:
    print("Adult")

# age < 7 >> pre-school
# age <= 12 >> output primary
# age <= 16 >> secondary
# age <= 18 >> jc
# else adult