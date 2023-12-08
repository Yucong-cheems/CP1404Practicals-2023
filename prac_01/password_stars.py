password = input("Enter your password: ")
password_length = 8
while len(password) < password_length:
    print("password error!")
    password = input(f"Enter your password with minimum {password_length} characters: ")

if len(password) > password_length:
    print(len(password) * '*')
    print("Thank you")