"""More scores program"""

from random import randint


def main():
    """Create a list of random scores of a user specified size then determine the result of each score and write it
    to a file."""
    number_of_scores = int(input("How many scores: "))
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        score = randint(0, 100)
        result = determine_score_category(score)
        print(f"{score} is {result}", file=out_file)
    out_file.close()


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
