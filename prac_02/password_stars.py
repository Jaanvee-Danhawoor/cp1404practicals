def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    minimum_length = 5
    password = input("Password: ")
    while len(password) < minimum_length:
        password = input("Password: ")
    return password


main()
