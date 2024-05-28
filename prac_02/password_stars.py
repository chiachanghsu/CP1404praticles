MINIMUN_LENGTH = 10


password = input("Enter your password: ")
while len(password) < MINIMUN_LENGTH:
    print("too short.")
    password = input("Enter your password: ")
print("*" * len(password))
