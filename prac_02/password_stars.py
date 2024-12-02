"""Password check program"""


def main():
    """Get valid password and print asterisks as long as the password"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks as long as the password"""
    print("*" * len(password))


def get_password():
    """Get password of length greater than or equal to minimum_length"""
    minimum_length = 5
    password = input("Password: ")
    while len(password) < minimum_length:
        password = input("Password: ")
    return password


main()
