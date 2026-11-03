"""
CP1404 - Practical
Program to determine score status using functions.
"""
import random


def main():
    """Get a score from the user and display the result,
    then show a random score result"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"User score {score} is {result}")
    # Or better formatting
    """print(f"User score {score:g} is {result}")"""
    
    if result == "Excellent":
        print("You win a prize!")

    random_score = random.randint(0, 100)
    print(f"Random: {random_score} = {determine_result(random_score)}")


def determine_result(score):
    """Return the result description for a given score """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
