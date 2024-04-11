width = int(input("How wide is the room in meters?\n"))
length = int(input("How long is the room in meters?\n"))
area = width * length


print(f"""Your room is {area} meters squared."
This is equivalent to {area * 10.7639:.2f} feet squared.""")