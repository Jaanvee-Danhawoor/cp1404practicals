MENU = "(G)et a valid score\n(P)rint result\n(S)how stars \n(Q)uit"


def main():
    print(f"Menu:\n{MENU}")
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice")
        print(f"Menu:\n{MENU}")
        choice = input("Choose: ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()
