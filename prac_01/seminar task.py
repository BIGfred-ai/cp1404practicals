"""
pseudo-

get price
get GST qualification
calculate new price
print new price formatted to currency


GST = 1.1

item_price = int(input("What is your item price?"))
GST_qualification = input("Does it have GST? Y/N ?")

if GST_qualification == "Y":
    total = item_price * GST
else: total = item_price

print(f"Your Total is ${total:.2f}")
"""
"""Example from instructor
GST_RATE = 1.1

item_price = float(input("Price: "))
gst_response = input("GST: ")
if gst_response == "yes":
    item_price *= (1 * GST_RATE)
print(f"${item_price:.2f}")
"""


