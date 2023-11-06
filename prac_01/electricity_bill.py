print("Electricity bill estimator")
cents = int(input("Enter cents per KWH: "))
while cents <= 0:
    print("input must > 0")
    cents = int(input("Enter cents per KWH: "))

daily_use = float(input("Enter daily use in KWH: "))
while daily_use <= 0:
    print("input must > 0")
    daily_use = float(input("Enter daily use in KWH: "))