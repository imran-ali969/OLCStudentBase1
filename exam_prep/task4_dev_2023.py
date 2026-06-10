
# Task 4 - 2023 Paper - Development of Program

# Open the file SPLIT_SENTENCE.py. You will see the following function that 
# takes a string of words, passed as the parameter word_string, splits it 
# into individual words and stores these words in a list. 
# It returns the list of words. 

# You can assume the string does not contain punctuation marks.

def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence



# # Task 4.1
# 10.	Save the program as CHECK_LIST_2023_<your name>_<centre number>_<index number>.py [7 marks]
# Extend the program by writing another function check_list() that searches 
# through the list of words to find a certain word. 

# If it finds the word in the list, it returns "Yes", otherwise it returns "No". 
# The variable word needs to be passed to the function. 
# The function you write must use the function split_sentence() already provided.
# Save your program.

#---------------------------------------
# Task 4.1 [7]
#---------------------------------------
# write your code here
def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence
    
def check_list(word, sentence):
    list_words = split_sentence(sentence) #uses split_sentence() function to help split
    if word in list_words:
        return "Yes"
    else:
        return "No"
print(check_list("hungry", "I am hungry"))

# # Task 4.2
# 11.	Save your program as REVERSE_2023_<your name>_<centre number>_<index number>.py [7 marks]
# Extend your program by writing another function reverse_sentence() 
# that reverses the words in the string and returns the whole string reversed, 
# with spaces between the words. 

# For example, 
# "the cat sat on the mat" would return: "mat the on sat cat the". 

# The function you write must use the function split_sentence() already provided. 
# You must not use the slice operator or the reverse function available in Python. 
# Your program does not need to consider any spaces before or after 
# the reversed sentence. Save your program.

# write your code here

#---------------------------------------
# Task 4.2 [7]
#---------------------------------------
def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence
    
def check_list(word, sentence):
    list_words = split_sentence(sentence)
    if word in list_words:
        return "Yes"
    else:
        return "No"
print(check_list("hungry", "I am hungry"))

def reverse_sentence(sentence):
    reverse = split_sentence(sentence)
    output = ""
    for word in reverse:
        output = word + " " + output #reverses by adding the words backwards instaed of using reverse and slicing
    return output
        
print(reverse_sentence("i am hungry"))




# # Task 4.3
# 12.	Save your program as FUNCTIONS_2023_<your name>_<centre number>_<index number>.py [6 marks]

# Extend your program by using the functions created such that it:
# •	allows the user to input a string of words (validation of this is not necessary)
# •	allows the user to input a word to search for in the string of words
# •	outputs the string of words, split into a list
# •	outputs the string of words, reversed
# •	outputs whether the word input is found in the string of words.
# Save your program.


#---------------------------------------
# Task 4.3 [7]
#---------------------------------------
string_of_words = input("Enter a string of words: ")
word_search = input("Enter a word: ")
print(split_sentence(string_of_words))
print(reverse_sentence(string_of_words))

word_exist = check_list(word_search, string_of_words)
if word_exist == "Yes":
    print(f"{word_search} exists in {string_of_words}")
else:
    print(f"{word_search} does not exists in {string_of_words}")
# •	allows the user to input a string of words (validation of this is not necessary)
# string_of_words = input("Enter a string of words: ")

# # •	allows the user to input a word to search for in the string of words
# word_search = input("Enter the word to search for: ")

# # •	outputs the string of words, split into a list
# print(split_sentence(string_of_words))

# # •	outputs the string of words, reversed
# print(reverse_sentence(string_of_words))

# # •	outputs whether the word input is found in the string of words.
# word_exist = check_list(word_search, string_of_words)
# if word_exist == "Yes":
#     print(f"{word_search} exists in {string_of_words}")
# else:
#     print(f"{word_search} does not exists in {string_of_words}")


    