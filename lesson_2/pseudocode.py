# 1. a function that returns the sum of two numbers 

# START

# GET value1 and value2 from user

# PRINT value1 + value2
# END



# 2. a function that takes a list of strings, and returns
# a string that is all those strings concatenated together

# START

# SET a list_of_strings

# SET concatenated_string as the first element of list_of_strings 

# FOR all the elements except the first in list_of_strings,
# SET concatenated_string += element

# PRINT concatenated_string
# END



# 3. a function that takes a list of integers, and returns a new list with
#every other element from the original list, starting with the first element.

# START

# SET int_list
# SET new_list = []
# SET counter = 0

# WHILE counter < (the number of elements - 1),
# APPEND new_list with int_list[counter]
# SET counter += 2 

# PRINT new_list
# END



# 4. a function that determines the index of the 3rd occurrence
# of a given character in a string.

# START

# SET string
# SET given_character
# SET counter = 0

# FOR all chars in string,
# IF char == given_character, counter += 1
# IF counter == 3, RETURN string[char]
# ELSE RETURN None


# 5. a function that takes two lists of numbers and returns the result of merging the lists.
# Elements of the first list should become the elements at the even indexes of the returned list,
# while the elements of the second list should become the elements at the odd indexes.

# START

# SET first_list
# SET second_list
# SET new_list = []
# SET counter = 0

#WHILE counter < the number of elements
#take the first_list[counter] and append it to new_list
#take the second_list[counter] and append it to new_list
#SET counter += 1

#PRINT new_list
