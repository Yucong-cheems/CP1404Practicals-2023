total_price = 0

items = int(input("Number of items: "))
while items < 0:
    print("Number of item must > 0")
    items = int(input("Number of items: "))

for i in range(0, items, 1):
    price_of_item = float(input("Price of item: "))
    while price_of_item < 0:
        print("Invalid input")
        price_of_item = float(input("Price of item: "))
    total_price += price_of_item


if total_price > 100:
    total_price -= total_price * 0.1

print(f"Total price for {items} is {total_price}")

