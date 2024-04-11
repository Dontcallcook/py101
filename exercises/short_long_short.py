#Get two strings from user
#Read length of strings
#Set larger string as larger_string and shorter string as shorter_string
#print shorter_string + larger_string + shorter_string

def empty_string_checker(string):
    while string.strip() == "":
        print("Please input a complete string.")
        print("Enter at least one character: ")
        string = input()
    return string

def string_combiner(string_1, string_2):
    if len(string_1) < len(string_2):
        print(string_1 + string_2 + string_1)
    else:
        print(string_2 + string_1 + string_2)


print("Enter string number 1: ")
string_1 = input()

string_1 = empty_string_checker(string_1)

print("Enter string number 2: ")
string_2 = input()

string_2 = empty_string_checker(string_2)

string_combiner(string_1, string_2)


