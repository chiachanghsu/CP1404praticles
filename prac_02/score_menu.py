MENU = ("(G)et a valid score (must be 0-100 inclusive)"
        "\n(P)rint result (copy or import your function to determine the result from score.py)"
        "\n(S)how stars (this should print as many stars as the score)"
        "\n(Q)uit")


def main():
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Your score is {score}.")
        elif choice == "P":
            grade = determine_grade(score)
            print(f"Your grade is {grade}.")
        elif choice == "S":
            print("*" * score)
        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell.")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid.")
        score = int(input("Enter score: "))
    return score


main()
