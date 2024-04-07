class Car:
    price = 1000000
    def horse_powers(self):
        return self

class Nissan(Car):
    price = 15
    def horse_powers(self):
        return self
class Kia(Car):
    price = 99999999
    def horse_powers(self):
       return self

print(Car.price, Car.horse_powers(999))
print(Nissan.price, Nissan.horse_powers(131))
print(Kia.price, Kia.horse_powers(1341))
