#how to define a dictionary
menu = {"spaghetti": 8.9, "passta": 15.5, "fries":5.9}

#retrieve value based on key
price = menu["fries"]
print(price)

#add to a dictionary
menu["burger"] = 9
print(menu)

#change a value in dictionary
menu["passta"] = 25
print(menu)

#delete from dictionary
del menu["passta"]
print(menu)

#check if smt exist in dictionary
check_list = "burger"
if check_list in menu:
    print(f"{check_list} is for sale")
else:
    print(f"{check_list} is not for sale")

#how to loop through a dictionary
for k in menu:
    print(f"{k} : ${menu[k]}")

#shortcut way to pull out both key and value
for item, price in menu.items():
    print(f"{item}: ${price}")



















dict1 = {"hamburger": 5, 
         "pasta": 10, 
         "fries": 2}

# add / amend
dict1["hamburger"] = 10

# for key,value in dict1.items():
#     print(key)
#     print(value)

# for key in dict1:
#     print(key) # key
#     print(dict1[key]) # value

def oddoreven(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
