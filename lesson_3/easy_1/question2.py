str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def end_in_exclamation(string):
    if string[-1] == "!":
        return True
    return False

print(end_in_exclamation(str1))
print(end_in_exclamation(str2))