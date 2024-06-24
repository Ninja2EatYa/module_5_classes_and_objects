class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        return self.numberOfFloors


print('NewNumberOfFloors:', House().setNewNumberOfFloors(8))
