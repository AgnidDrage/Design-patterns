from CarType import CarType
from Location import Location
from LuxuryCar import LuxuryCar
from SmallCar import SmallCar
from Car import Car


class USACarFactory:
    
    def buildCar(self, model):
        if model == CarType.LUXURY:
            car = LuxuryCar().LuxuryCar(location=Location.USA)
        
        elif model == CarType.SMALL:
            car = SmallCar().SmallCar(location=Location.USA)
        
        return car