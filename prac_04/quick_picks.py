import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_PER_QUICK_PICK = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        numbers = []
        while len(numbers) < NUMBER_PER_QUICK_PICK:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            if number not in numbers:
                numbers.append(number)
            numbers = sorted(numbers)
        print(" ".join(f"{number:2d}" for number in numbers))


main()
