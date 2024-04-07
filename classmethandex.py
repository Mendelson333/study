class Building:
    total = 0
    def __init__(self):
        Building.total += 1

buildings = []
buildrange = 40
while len(buildings) < buildrange:
    new_Building = Building()
    buildings.append(new_Building)
print(Building.total)
