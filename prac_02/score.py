"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
REPEAT_TIME = 10
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(f"Your score is {grade}")
    for i in range(REPEAT_TIME):
        score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
        grade = determine_grade(score)
        print(f"{score} is {grade}")


def determine_grade(score):
    if score < 50:
        return "Bad"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Excellent"


main()
