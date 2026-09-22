"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))

if 0 <= score <= 100:
    score_qualification = "Valid"

    if score < 50:
        score_reply = "Bad news buster"
    elif score <= 90:
        score_reply = "Passable"
    else:
        score_reply = "Excellent"

else:
    score_qualification = "Invalid"
    score_reply = "No grade because score is invalid"

print(f"{score_qualification}, {score_reply}")

