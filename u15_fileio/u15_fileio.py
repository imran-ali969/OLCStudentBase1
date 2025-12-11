#create a file
with open("text1.txt", "w") as file:
    file.write("hello world") #write 

# read a file
with open("text1.txt", "r") as file:
    context = file.read()

print(context)