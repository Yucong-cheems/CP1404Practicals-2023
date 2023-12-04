
def main():
    MENU = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius 
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            Celsius_to_Fahrenheit(celsius)
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            Fahrenheit_to_Celsius(fahrenheit)
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def Fahrenheit_to_Celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"result: {celsius:.2f} C")


def Celsius_to_Fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
