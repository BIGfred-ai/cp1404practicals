"""CP1404 Prac_04
Lottery ticket generator"""

import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_picks = int(input("How many quick-picks? "))
    for i in range(number_of_picks):
        pick = generate_pick()
        print("".join(f"{number:2d}" for number in pick))


def generate_pick():
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in pick:
            pick.append(number)
            pick.sort()
    return pick


main()
