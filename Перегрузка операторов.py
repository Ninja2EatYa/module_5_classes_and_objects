class Building:
    def __init__(self, name, dots, numberOfFloors, _sub, buildingType):
        self.name = name
        self.dots = dots
        self.numberOfFloors = int(numberOfFloors)
        self._sub = _sub
        self.buildingType = str(buildingType)
        print(f'{self.name}', self.dots, self.numberOfFloors, self._sub, self.buildingType)

    def __eq__(self, other):
        print(f'Кол-во этажей у {self.name} и {other.name} одинаковое:', self.numberOfFloors == other.numberOfFloors)
        print(f'Типы зданий {self.name} и {other.name} одинаковые:', self.buildingType == other.buildingType)


B1 = Building('B1', ':', 30, 'этажей, тип', 'Монолит')
B2 = Building('B2', ':', 30, 'этажей, тип', 'Кирпич')

B1 == B2