MENU = "(G)et a valid score\n(P)rint result\n(S)how stars \n(Q)uit"


def main():
    print(f"Menu:\n{MENU}")
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice")
        print(f"Menu:\n{MENU}")
        choice = input("Choose: ").upper()
    print("Farewell")


main()
