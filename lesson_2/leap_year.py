#if year < 1752
#If the year is divisible by 400, it is a leap year.
#If the year is divisible by 100 but not by 400, it is not a leap year. 
#If the year is divisible by 4 but not by 100, it is a leap year.

def leap_year(year):
    if year < 1752 and year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print("What year would you like to check?")
year = input()

try:
    int(year)
except ValueError:
    print("Please input a digit as the year, e.g., 100, 150, etc.")
    year = input()

print(leap_year(int(year)))


    