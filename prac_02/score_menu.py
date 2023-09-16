"""Score Menu Program

Psuedocode:

MENU = (G)et a valid score, (P)rint result, (S)how stars, (Q)uit
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

score = get_valid_number(MINIMUM_SCORE,MAXIMUM_SCORE)
print MENU
get menu_choice
while menu_choice != Q
    if menu_choice = G
        score = get_valid_number(MINIMUM_SCORE,MAXIMUM_SCORE)
    else if menu_choice = P
        score_category = determine_score_category
        print score_category
    else if menu_choice = S
        print_line_of_characters()
    else
        print error message
    print MENU

function get_valid_number(low, high)
    get score
    while score < low or > high
        print error message
        get score
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    print("Welcome to the Score Menu")
    score = get_valid_number("Enter score: ", MINIMUM_SCORE, MAXIMUM_SCORE)
    print(MENU)
    choice = input("What would you like to do?: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("Enter score: ", MINIMUM_SCORE, MAXIMUM_SCORE)
        elif choice == "P":
            score_category = determine_score_category(score)
            print(score_category)
        elif choice == "S":
            print_line_of_characters(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("What would you like to do?: ").upper()
    print("Farewell")


def get_valid_number(prompt, low, high):
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = int(input(prompt))
    return number


def determine_score_category(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"


def print_line_of_characters(length, character="*"):
    print(character * length)


main()
