"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
bonus_rate_low = 0.10
bonus_rate_high = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:

    if sales < 1000:
        sales_total = sales * bonus_rate_low
    else:
        sales_total = sales * bonus_rate_high

    print(f"{sales_total:.2f}")

    sales = float(input("Enter sales: $"))

if sales <= 0:
    print(f"Work harder!")
