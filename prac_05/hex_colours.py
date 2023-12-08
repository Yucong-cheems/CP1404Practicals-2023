"""
hex_colours
Estimate: 20 minutes
Actual:   10 minutes
"""

color = {"Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
         "AntiqueWhite2": "#eedfcc",
         "AntiqueWhite3": "#cdc0b0"}
print(color)
while True:
    color_name = input("Enter a color name: ").title()

    while color_name != " ":
        if color_name in color:
            color_code = color.get(color_name)
            print(color_name, "is", color_code)

        else:
            print("invalid input")

        color_name = input("Enter a color name: ").title()