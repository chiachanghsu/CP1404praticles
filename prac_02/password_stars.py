MINIMUN_LENGTH = 10


def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    password = input("Enter your password: ")
    while len(password) < MINIMUN_LENGTH:
        print("too short.")
        password = input("Enter your password: ")
    return password


main()
