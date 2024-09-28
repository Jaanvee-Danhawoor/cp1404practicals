"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
