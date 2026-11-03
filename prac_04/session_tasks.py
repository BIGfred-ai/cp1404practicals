"""Retrives chosen name and prints as a number"""
from operator import itemgetter

"""psuedo
list names
get name
print related number 

NAMES = ["DICK","JANE","ALICE","BOB"]

print()"""

#whats wrong with this student answer to prac 3 q4
#how can we improve it

#with open("numbers.txt", "r") as input_file
#	numbers = input_file.readlines()
#	sum-of_numbers = 0
#	for number in numbers:
#		sum_of_numbers += float(number)
#	print(f"Total sum of numbers is {sum_of_numbers}")

#my turn :
#with open("numbers.txt", "r") as input_file
#	lines = input_file.readlines()
#total = 0
#for line in input_file:
#	total += float (number)
#print(f"Total sum of numbers is {total}")


name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantenelle': 9}
width = max(len(name) for name in name_to_score)

for name, score in name_to_score:
    print(f"{name:{width}} = {score:3}")

    """
for name in sorted(name_to_score, key=itemgetter(1), reverse=True):
    print(f"{name:{width}} = {name_to_score[name]:3}")
    """
"""
max_number_width = max((len(str(pair[1]))) for pair in name_to_score)

print(max_name_width)
print(max_number_width)

for name, number in data:
    print(f"{name}:< (max_name_width) = {number}:> (max_number_width)")
"""


