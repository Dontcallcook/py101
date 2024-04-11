#GET int greater than 0 from user
#Ask if the user wants the sum or product of all integers between 1 and number inclusive
#Calculate sum or product

def sum_calculator(number_list):
    total = 0
    for number in int_list:
        total += number
    print(f"The sum of the integers between {int_list[0]} "
    f"and {int_list[-1]} is {total}.")
    
def product_calculator(number_list):
    total = 1
    for number in int_list:
        total *= number
    print(f"The product of the integers between {int_list[0]} " 
    f"and {int_list[-1]} is {total}.")

print("Please enter an integer greater than 0: ")
user_int = input()

while True:
    try:
        int(user_int)
    except ValueError:
        print("Sorry, you must input a number greater than 0: ")
        user_int = input()
    else:
        if int(user_int) > 0:
            break
        else:
            print("Sorry, you must input a number greater than 0: ")
            user_int = input()

print("Please choose your caluclation by typing 'sum' or 'product'")
user_calc = input()

while user_calc not in ["sum", "product"]:
    print("Your calculation was not recognised."
    "Please type 'sum' or 'product'")
    user_calc = input()

int_list = list(range(1, (int(user_int) + 1)))

if user_calc == "sum":
    sum_calculator(int_list)
else:
    product_calculator(int_list)
    

    
    
    
    