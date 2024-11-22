from prac_09.silver_service_taxi import SilverService


def main():
    """Test SilverService Taxi."""
    silver_service_taxi = SilverService("Silver Taxi", 100, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(f"For an 18 km trip in a SilverService taxi with fanciness 2, the fare should be $48.78 is "
          f"${silver_service_taxi.get_fare():.2f}")


main()
