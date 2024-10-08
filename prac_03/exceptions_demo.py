"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If the user inputs a value for either the numerator or denominator that cannot be converted to an integer.
2. When will a ZeroDivisionError occur?
denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by checking if the denominator is 0 before doing the computation in the try suite.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
