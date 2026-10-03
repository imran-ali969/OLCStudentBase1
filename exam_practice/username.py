firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
username = firstname[0:3] + lastname
print("Your username is " + username)
while True:
    password = input("Please enter a password: ")
    if len(password) < 8:
        print("Password must be more than 8 characters")
    else:
        break
password2 = input("Please reenter a password: ")
while True:
    if password == password2:
        print("Your password has been set.")
        break
    else:
        password2 = input("Password entries do not match. Please repeat the second entry of your password: ")
