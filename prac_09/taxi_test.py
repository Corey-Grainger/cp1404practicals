"""CP1404 Week 09 Pracs
Taxi Class Test Program
Estimate: 15 minutes
Commenced: 10:10am
Completed: 10:21am"""

from taxi import Taxi

my_taxi = Taxi("Prius", 100)
my_taxi.drive(40)
print(my_taxi)
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
current_fare = my_taxi.current_fare_distance * my_taxi.price_per_km
print(f"Current fare for {my_taxi.name} is ${current_fare:.2f}")
