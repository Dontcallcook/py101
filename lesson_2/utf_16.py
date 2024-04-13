def utf16_value(string):
    total = 0
    for char in string:
        total += ord(char)
    return total

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)
