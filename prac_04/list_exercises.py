def main():
    number = []
    for i in range(5):
        try:
            numbers = int(input("Number: "))
        except ValueError:
            print("Invalid value")
            numbers = int(input("Number: "))
        number.append(numbers)

    print(f"The first number is {number[0]}")
    print(f"The last number is {number[-1]}")
    print(f"The smallest number is {min(number)}")
    print(f"The largest number is {max(number)}")
    print(f"The average number is {sum(number) / len(number)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()