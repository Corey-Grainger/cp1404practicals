
"""
get start_number, end_number
display menu
get menu_choice
while menu_choice != Q
    if menu_choice = E

    else if menu_choice = O

    else if menu_choice = S

    else
        print error message
    get menu_choice
print farewell message
"""


MENU = "(E)ven numbers\n(O)dd numbers\n(S)quares\n(Q)uit"


def main():
    start_number = int(input("Enter start number: "))
    end_number = int(input("Enter end number: "))
    sequence_direction = determine_sequence_direction(start_number, end_number)
    print(MENU)
    menu_choice = input("What would you like to do?: ").upper()
    while menu_choice != "Q":
        if menu_choice == "E":
            for i in range(start_number, end_number + sequence_direction, sequence_direction):
                if i % 2 == 0:
                    print(i)
        elif menu_choice == "O":
            for i in range(start_number, end_number + sequence_direction, sequence_direction):
                if i % 2 == 1:
                    print(i)
        elif menu_choice == "S":
            for i in range(start_number, end_number + sequence_direction, sequence_direction):
                print(i ** 2)
        else:
            print("Invalid selection")
        print(MENU)
        menu_choice = input("What would you like to do?: ").upper()
    print("Farewell")


def determine_sequence_direction(start_number, end_number):
    if start_number > end_number:
        return -1
    return 1


main()
