"""Score Menu Program"""
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars \n(Q)uit"


def main():
    """Menu-driven program about valid scores"""
    score = get_valid_score()
    print(f"Menu:\n{MENU}")
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(f"Menu:\n{MENU}")
        choice = input("Choose: ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def print_result(score):
    """Print result based on store"""
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print("Excellent")


def show_stars(score):
    """Print as many stars as score"""
    print("*" * score)


main()
