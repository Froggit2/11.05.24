class Home:

    Floor = 1

    def __init__(self):
        self.Floor = 1


Home.numberOfFloors = 10
for Home.Floor in range(Home.numberOfFloors):
    print("Текущий этаж равен", Home.Floor)
    Home.Floor += 1
