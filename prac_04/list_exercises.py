# Numbers list
numbers = []
print("Enter 5 numbers")
for i in range(1, 6):
    number = int(input("Number: "))
    numbers.append(number)
first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average_number = sum(numbers) / len(numbers)
print(f"The first number is {first_number}")
print(f"The last number is {last_number}")
print(f"The smallest number is {smallest_number}")
print(f"The largest number is {largest_number}")
print(f"The average of the numbers is {average_number}")

# 2. Woefully inadequate security checker...
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
