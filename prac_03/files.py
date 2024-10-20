# 1
name = input("Name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()
# 2
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")
# 3
with open("numbers.txt", "r") as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
result = number_1 + number_2
print(result)
# 4
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += float(line.strip())
print(f"Total: {total}")

