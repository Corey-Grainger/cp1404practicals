""" CP1404 Week 5 Practical
 Hex Colours Program"""

NAME_TO_HEX_CODE = {"Candy Apple Red": "#ff0800", "Banana Yellow": "#ffe135", "Banana Mania": "#fae7b5",
                    "Apricot": "#fbceb1", "Asparagus": "#87a96b", "Bitter Lime": "#bfff00", "Black Olive": "#3b3c36",
                    "Boysenberry": "#873260", "Carrot Orange": "#ed9121", "Deep Peach": "#ffcba4",
                    "Eggplant": "#614051", "Granny Smith Apple": "#a8e4a0", "Mango Tango": "#ff8243"}

print(NAME_TO_HEX_CODE)
name = input("Enter colour name: ").title()
while name != "":
    try:
        print(f"{name} is {NAME_TO_HEX_CODE[name]}")
    except KeyError:
        print("Invalid colour name")
    name = input("Enter colour name: ").title()
print("Colour your world!")
