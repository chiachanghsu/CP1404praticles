TIMES = 2

def question_1():
    out_file = open("names.txt", "w")
    name = input("Enter your name: ").title()
    print(name, file=out_file)
    out_file.close()


def question_2():
    in_file = open("names.txt", "r")
    for line in in_file:
        print(f"Hi {line.strip()}!")
    in_file.close()


def question_3():
    number = 0
    with open("numbers.txt", "r") as in_file:
        for i in range(TIMES):
            line = int(in_file.readline())
            number += line
        print(number)


def question_4():
    number = 0
    with open("numbers.txt", "r") as in_file:
        for line in in_file:
            line = int(line)
            number += line
        print(number)


question_1()
question_2()
question_3()
question_4()
