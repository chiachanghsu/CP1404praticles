"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)


def determine_grade(score):
    if score < 50:
        return "Bad"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Excellent"


main()
