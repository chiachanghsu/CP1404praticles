MENU = ("(G)et a valid score (must be 0-100 inclusive)"
        "\n(P)rint result (copy or import your function to determine the result from score.py)"
        "\n(S)how stars (this should print as many stars as the score)"
        "\n(Q)uit")


def main():
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_vaild_score()
            print(f"Your score is {score}")
        elif choice == "P":
            if score == "":
                print("Where is your score?")
            else:
                grade = determine_grade(score)
                print(f"Your grade is {grade}")
        elif choice == "S":
            print("*" * score)
        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell.")
