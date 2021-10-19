from Car import Car
import CarType


class SmallCar(Car):
    def SmallCar(self, location):
        self.construct()
        return Car(CarType.CarType.SMALL, location)
        
    def construct(self):
        print('Building small car')
