class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


home1 = Building(numberOfFloors=10,buildingType="Кирпичный дом")
home2 = Building(numberOfFloors=5, buildingType="Панельный дом")
if Building.__eq__(self=home1,other=home2 ):
    print("Два одинаковых дома очуметь")
else: print("А дома то разные")
