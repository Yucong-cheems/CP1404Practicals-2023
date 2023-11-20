password = input("Enter your password: ")
while True:
    if len(password) <= 6:
        print("too short!")
    else:
        print('*' * len(password))
    password = input("Enter your password: ")
