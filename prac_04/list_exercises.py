"""CP1404 Week 4 Practicals List exercises program"""

# Basic List Operations
numbers = []
for i in range(5):
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input("Number: "))
            is_valid_number = True
        except ValueError:
            print("Number must be a valid integer")
    numbers.append(number)  # Error checking ensures number is defined
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
