"""
emails
Estimate: 10 minutes
Actual:   20 minutes
"""


def main():
    email_name = {}
    email = input("Email: ")
    while email != " ":
        username = extraction(email)
        check = input(f"Is your name {username}? (Y/N)")
        if check.upper() != "Y" and check != " ":
            username = input("name: ")
        email_name[email] = username
        email = input("Email: ")

    for email, username in email_name.items():
        print(f"{username}({email})")


def extraction(email):
    name = email.split("@")[0]
    part = name.split(".")
    full_name = " ".join(part).title()
    return full_name


main()