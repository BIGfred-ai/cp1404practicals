def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Enter password: ")
    while len(password) == 0:
        print("Password cannot be empty.")
        password = input("Enter password: ")
    return password


def print_stars(password):
    print("*" * len(password))


main()
