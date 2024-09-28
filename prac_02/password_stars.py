minimum_length = 5
password = input("Password: ")
while len(password) < minimum_length:
    password = input("Password: ")
print("*" * len(password))
