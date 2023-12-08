name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(f"your name is: {name}", file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is{name}")

#with open("name.txt", "r") as in_file:
    #name = in_file.read().strip()
#print("Your name is", name)

in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)