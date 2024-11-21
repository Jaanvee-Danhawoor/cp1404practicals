from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class."""
    my_unreliable_car = UnreliableCar("My car", 100, 80)
    print(my_unreliable_car)
    my_unreliable_car.drive(20)
    print(my_unreliable_car)


main()
