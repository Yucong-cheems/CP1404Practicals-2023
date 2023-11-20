def main():

    score = float(input("Enter score:  "))
    print(determine_status(score))


def determine_status(score):
    while True:
        if score < 0 or score > 100:
            print("Invalid score")
        elif score >= 50:
            print("Passable")
        elif score >= 90:
            print("Excellent")
        else:
            print("Bad")
        score = float(input("Enter score: "))


main()