for i in range(1, 21, 2):
    print(i, end=' ')
print()

for k in range(0, 101, 10):
    print(k, end=' ')
print()

for j in range(20, 0, -1):
    print(j, end=' ')
print()

number = int(input("Enter a number: "))
print(f"Number of stars: {number}\n{number * '*'}")

row = int(input("Enter number of row: "))
for i in range(1, row+1, 1):
    print("*" * i)

