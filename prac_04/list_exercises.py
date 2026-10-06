"""CP1404 Prac_04
List operation and security checker"""
# part 1
numbers = []
for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

print(f"the first number is {numbers[0]:.0f}")
print(f"The last number is {numbers[-1]:.0f}")
print(f"The smallest number is {min(numbers):.0f}")
print(f"The largest number is {max(numbers):.0f}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


# part 2
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied!")
