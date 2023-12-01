
"""
DISCOUNT_RATE = 0.1
get number_of_items
repeat number_of_items times
    get item_price
    total += item_price
if total > 100
    total -= total * DISCOUNT_RATE
print total
"""

DISCOUNT_RATE = 0.1
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total = 0
for i in range(number_of_items):
    item_price = float(input("Item price: $"))
    total += item_price
if total > 100:
    total -= total * DISCOUNT_RATE
print(f"Total price for {number_of_items} is ${total:.2f}")
