"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Get a score and print the score category, then print the score category of a random score."""
    score = float(input("Enter score: "))
    score_category = determine_score_category(score)
    print("The entered score is", score_category)
    score_category = determine_score_category(random.randint(0, 100))
    print("The randomly generated score is", score_category)


def determine_score_category(score):
    """Determine the result category of score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"


main()
