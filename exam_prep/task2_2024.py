######### LOGIN.py #########
# list_username = ["StudentNo1", "JaneJones", "ABC123"] 
# username = input("Please enter a username: ")
# password = input("Please enter a password: ") 

# Task 1.1 #######################
# 4 marks
list_username = ["StudentNo1", "JaneJones", "ABC123"] 
while True:
    username = input("Please enter a username: ") 
    if username in list_username:
        print("Enter another username.")
    else:
        list_username.append(username)
        break
password = input("Please enter a password: ") 
# print(list_username)





# Task 1.2 #######################

special_char = ["@","!","/","?"]
list_username = ["StudentNo1", "JaneJones", "ABC123"] 
while True:
    username = input("Please enter a username: ") 
    if username in list_username:
        print("Enter another username.")
    else:
        list_username.append(username)
        break

        
while True:
    password = input("Please enter a password: ") 
    for i in password:
        if len(password) == 8 and i in special_char:
            break
   