"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Print score status given score"""
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)
    random_score = random.randint(0, 100)
    random_score_status = determine_score_status(random_score)
    print(random_score_status)


def determine_score_status(score):
    """Determine score status"""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
