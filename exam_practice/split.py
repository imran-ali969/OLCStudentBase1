def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence
def check_list(word_string, word):
    list_sentence = split_sentence(word_string)
    for item in list_sentence:
        if item == word:
            return "Yes"
    return "No"
def reverse_sentence(word_string):
    list_sentence = split_sentence(word_string)
    reversed_sentence = ""
    for i in list_sentence:
        reversed_sentence = i + " " + reversed_sentence
    return reversed_sentence

word_string = input("Enter a string of words: ")
word = input("Enter a word: ")
print(split_sentence(word_string))
print(reverse_sentence(word_string))
print(check_list(word_string, word))