class House:
    def __init__(self):
        self.NumberOfFloors = 0;
    def setNewNumberOfFloors(floors):
        House.NumberOfFloors = floors
        print(House.NumberOfFloors)

House.setNewNumberOfFloors(10)