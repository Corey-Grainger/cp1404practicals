
"""
print welcome message
get price_per_kwh, daily_use, days_in_billing_period, connection_cost
estimated_bill = (price_per_kwh * daily_use * days_in_billing_period + connection_cost) / 100
print estimated_bill
"""

TARIFF_11 = 24.4618
TARIFF_31 = 13.6928

print("Electricity bill estimator 2.0")
tariff_category = int(input("Enter your tariff (11 or 31): "))
while tariff_category != 11 and tariff_category != 31:
    print("Invalid tariff")
    tariff_category = int(input("Enter your tariff (11 or 31): "))
if tariff_category == 11:
    price_per_kwh = TARIFF_11
else:
    price_per_kwh = TARIFF_31
daily_use = float(input("Enter daily use n kWh: "))
days_in_billing_period = int(input("Enter number of billing days: "))
connection_fee = float(input("Enter your connection fee in dollars: $"))
estimated_bill = price_per_kwh * daily_use * days_in_billing_period / 100 + connection_fee
print(f"Estimated bill: ${estimated_bill:.2f}")

