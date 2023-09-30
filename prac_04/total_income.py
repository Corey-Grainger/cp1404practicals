"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numbers_of_months = int(input("How many months? "))

    for month in range(1, numbers_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Print income report from incomes"""
    total = 0
    print("\nIncome Report\n-------------")
    for i, income in enumerate(incomes):
        total += income
        print(f"Month {i:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()