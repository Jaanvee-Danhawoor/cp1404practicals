from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_available_taxis(taxis)
            current_taxi = get_current_taxi(taxis)
        elif choice == "d":
            if current_taxi is not None:
                distance_to_be_driven = int(input("Drive how far? "))
                distance_driven = current_taxi.drive(distance_to_be_driven)
                fare = current_taxi.get_fare(distance_driven)
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
                fare = 0
            bill += fare
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill}")
    print("Taxis are now: ")
    display_available_taxis(taxis)


def get_current_taxi(taxis):
    index = int(input("Choose taxi: "))
    try:
        return taxis[index]
    except IndexError:
        print("Invalid taxi choice")


def display_available_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
