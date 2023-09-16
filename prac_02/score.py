"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    score_category = determine_score_category(score)
    print(score_category)


def determine_score_category(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"


main()
