"""The program allows the user to enter the
number of items and the price of each different item.
Then the program computes and displays the total price
 of those items.
If the total price is over $100, then a 10% discount
 is applied to that total
before the amount is displayed on the screen."""
"""
pseudo:
get items, and processor
if price is over $100 apply 10% discount
print total
"""
number_of_items = int(input("How many items?: "))
while number_of_items < 0:
    print(f"Invalid number of items")

total = 0
number_of_things = 0
repeat <somehow>
    get/determine/generate/calculate value
    total = total + value
    number_of_things += 1
average = total / number_of_things
print total, average
