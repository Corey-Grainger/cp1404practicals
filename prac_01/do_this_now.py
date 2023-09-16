
"""
while players want to play
    player with ball asks if player without ball is ready
    player without ball tells player with ball when they are ready
    player with ball throws the ball
    player without ball catches the ball

"""

"""
get monthly_cost
yearly_cost = monthly_cost * 12
print yearly_cost
"""

# monthly_cost = float(input("Monthly Service Cost: $"))
# yearly_cost = monthly_cost * 12
# print(f"The yearly cost is ${yearly_cost:.2f}")

"""

get gross_pay, tax_rate
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_amount
print net_pay
 
"""

# gross_pay = float(input("Enter gross pay: $"))
# tax_rate = float(input("Enter tax rate (e.g. 0.3): "))
# tax_amount = gross_pay * tax_rate
# net_pay = gross_pay - tax_amount
# print(f"Your net pay will be ${net_pay:.2f}")


# age = int(input("Age: "))
# while age < 0 or age > 120:
#     print("Invalid age")
#     age = int(input("Age: "))
# if age < 5:
#     category = "a baby"
# elif age < 18:
#     category = "a child"
# elif age < 66:
#     category = "an adult"
# else:
#     category = "old"
# print(f"You are {category}")


# SECRET = 4
# guess = int(input("Guess: "))
# while guess != SECRET:
#     print("Wrong. Try again!")
#     guess = int(input("Guess: "))
# print("Correct!")

# 1. definite
# 2. Indefinite
# 3. definite
# 4. definite
# 5. indefinite

# number_of_ages = int(input("How many ages?: "))
# total_age = 0
# for i in range(number_of_ages):
#     age = int(input("Enter age: "))
#     total_age += age
# average_age = total_age / number_of_ages
# print(f"The total age of people in the room is {total_age} and the average age is {average_age}")


count = 1
total_age = 0
age = int(input("Enter age: "))
while age >= 0:
    total_age += age
    count += 1
    age = int(input("Enter age: "))
average_age = total_age / count
print(f"The total age of people in the room is {total_age} and the average age is {average_age}")

