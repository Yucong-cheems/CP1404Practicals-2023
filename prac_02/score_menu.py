def main():
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>>Enter choice: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(score)
        elif choice == "P":
            determine_status(score)
        elif choice == "S":
            print_star(score)
        else:
            print("Invalid input!")
        print(MENU)
        choice = input(">>>Enter choice: ").upper()


def get_score():
    score = float(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = float(input("Enter a score: "))
    return int(score)


def determine_status(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    return score


def print_star(score):
    print(score * '*')


main()