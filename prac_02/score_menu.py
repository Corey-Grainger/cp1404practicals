"""Score Menu Program

Psuedocode:

MENU = (G)et a valid score, (P)rint result, (S)how stars, (Q)uit

score = get_valid_score()
print MENU
get menu_choice
while menu_choice != Q
    if menu_choice = G
        score = get_valid_score()
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

def main():
    score = 50
    print(MENU)
    choice = input("What would you like to do?: ").upper()
    while choice != "Q":
        if choice == "G":
            print("Get a valid score")
        elif choice == "P":
            print("score category")
        elif choice == "S":
            print("Stars")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("What would you like to do?: ").upper()
    print("Farewell")


main()
