#GET number
#SET list
#Extract all number if multiple of 3 or 5


def multi_sum(number):
    sum_list = list(range(1, number + 1))
    multiple_list = []
    total = 0
    for number in sum_list:
        if number % 3 == 0 or number % 5 == 0:
            multiple_list.append(number)
    for number in multiple_list:
        total += number
    return total

# These examples should all print True
print(multi_sum(3) == 3)
print(multi_sum(5) == 8)
print(multi_sum(10) == 33)
print(multi_sum(1000) == 234168)