from guitar import Guitar


def main():
    guitar = []
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add = Guitar(name, year, cost)
        guitar.append(add)
        print(add, "added")
        guitar.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitar.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        name = input("Name: ")


main()