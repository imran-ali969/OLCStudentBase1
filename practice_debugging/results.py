
name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0#start at 0 

flag = True
while flag == True:#they say if N glag becomes false but if Flag equals to false a new person is added
    name = input("Enter student's name: ")# ' in student's closed the string
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100:#should be and instead of or
            break
        else:
            print('Invalid mark!')
    mark_list += [mark]#shld not be dented
    count += 1
    if mark >= 75:#they say 75 or more is dist
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name]#should be []
    more = input('Would you like to enter another score, Y or N?: ')#Y and N should be a str
    if more == 'N':
        flag = False
print(mark_list)
average = round(sum(mark_list)/len(mark_list), 2)#shld be sum since we finding average
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.")#convert from int to str
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))