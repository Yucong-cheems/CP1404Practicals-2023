print("Electricity bill estimator")
cents = int(input("Enter cents per KWH: "))
while cents <= 0:
    print("input must > 0")
    cents = int(input("Enter cents per KWH: "))

daily_use = float(input("Enter daily use in KWH: "))
while daily_use <= 0:
    print("input must > 0")
    daily_use = float(input("Enter daily use in KWH: "))

Number_of_billing = int(input("Enter number of billing days:"))
while Number_of_billing <= 0:
    print("input must > 0")
    Number_of_billing = int(input("Enter number of billing days:"))

Bill = (cents/100) * daily_use * Number_of_billing
print(f"Estimated bill: ${Bill}")