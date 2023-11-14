"""CP1404 Week 09
Testing Program for Silver Service Taxi class"""

from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi(2, name="Hummer", fuel=500)
my_taxi.start_fare()
my_taxi.drive(18)
print(my_taxi)
print(f"Current fare for {my_taxi.name} is ${my_taxi.get_fare():.2f}")
