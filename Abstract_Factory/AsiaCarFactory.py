from Car import Car
import CarType
from Location import Location
from LuxuryCar import LuxuryCar
from SmallCar import SmallCar


class AsiaCarFactory:
    
    def buildCar(self, model):
        if model == CarType.CarType().LUXURY:
            car = LuxuryCar().LuxuryCar(location=Location.ASIA)
        
        elif model == CarType.CarType().SMALL:
            car = SmallCar().SmallCar(location=Location.ASIA)
        
        return car