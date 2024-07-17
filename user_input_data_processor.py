# Task 1
first_name = input("Please type your first name: ")
while len(first_name) < 2:
    print("Error! First name must be at least 2 characters long.")
    first_name = input("Please type your first name again: ")

last_name = input("Please type your last name: ")
while len(last_name) < 2:
    print("Error! last name must be at least 2 characters long.")
    last_name = input("Please type your last name again: ")

print(first_name, last_name)