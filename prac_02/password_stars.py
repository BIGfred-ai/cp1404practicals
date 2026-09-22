"""
program that asks the user for a low and a high number,
ensuring the high is higher than the low.
then print n smiley faces :) where n is a random number between low and high inclusive.
"""
from random import randint

# get number (high) and get number (low)
# check the high number is actually higher than the lower
# select a random nmber between low and
# high inlcusive and print that amount of smiley faces (n)

def main():
    low = int(input("Enter low number: "))
    high = int(input("Enter high number: "))

# ensure high is higher than low
    while high <= low:

        print("High number must be greater than low number.")
        high = int(input("Enter high number: "))

# Pick random number between low and high inclusive
    n = randint(low, high)

# print smiley faces
    print("Here are your smiles baby: ")
    print(":)" * n)

main()


