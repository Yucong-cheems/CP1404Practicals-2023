def main():
    password, password_length = get_password()

    check_the_password(password, password_length)


def check_the_password(password, password_length):
    if len(password) > password_length:
        print(len(password) * '*')
        print("Thank you")


def get_password():
    password = input("Enter your password: ")
    password_length = 8
    while len(password) < password_length:
        print("password error!")
        password = input(f"Enter your password with minimum {password_length} characters: ")
    return password, password_length


main()