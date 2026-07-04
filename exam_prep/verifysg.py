
ID = ""
count = 0
for i in range(5):
    ID = input("Enter ID: ")
    while True:
        if len(ID) == 9:
            print("ID is valid")
        else:
            print("ID is invalid.")
    if ID[0] == "S" or ID[0] == "T":
        print("Welcome home!")
        count += 1
    else:
        print("Welcome to Singapore!")
print(f"Total number of Singaporeans: {count} ")
