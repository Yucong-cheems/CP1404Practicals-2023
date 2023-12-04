import random

number = []
Number = 0
Number_of_picks = 6
number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    for k in range(Number_of_picks):
        Number = random.randint(1, 45)
        while Number in number:
            Number = random.randint(1, 45)
        number.append(Number)

    for k in number:
        print("{: >3}".format(k), end=" ")
    print()