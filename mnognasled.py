class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000
    def horse_powers(self):
        return self
class Nissan(Vehicle,Car):
    price = 10000
    vehicle_type = "Roadster"
    def horse_powers(self):
        return self

z350 = Nissan()
print(z350.vehicle_type, z350.price)
