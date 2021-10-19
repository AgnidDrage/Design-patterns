import CarType
from Car import Car
from Location import Location


class LuxuryCar(Car):
    def LuxuryCar(self, location):
        self.construct()
        return Car(CarType.CarType.LUXURY, location)

    def construct(self):
        print('Building luxury car')