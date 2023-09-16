
"""
Get available_number_of_gifts
Get number_of_students
Number_of_gifts_per_student = available_number_of_gifts // number_of_students
Number_of_gifts_left_over = available_number_of_gifts % number_of_students
Print number_of_gifts_per_student , number_of_gifts_left_over
"""

# number_of_gifts_available = int(input("Number of gifts to distribute: "))
# number_of_students = int(input("Number of students: "))
# number_of_gifts_per_student = number_of_gifts_available // number_of_students
# number_of_gifts_leftover = number_of_gifts_available % number_of_students
# print(f"Each student will get {number_of_gifts_per_student} and there will be {number_of_gifts_leftover} left over")

"""
get item_price, gst_category
if gst+category = y
    item_price = item_price * 1.1
print item_price
"""

item_price = float(input("Item price: $"))
gst_category = input("Does item incur GST (Y/n)?: ").upper()
if gst_category == "Y":
    item_price = item_price * 1.1
print(f"Your final price is ${item_price}.2f")
