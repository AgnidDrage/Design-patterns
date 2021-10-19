from Location import Location
from Car import Car
import AsiaCarFactory
from enum import Enum
import USACarFactory

class CarType():
    SMALL = 'SMALL'
    LUXURY = 'LUXURY'

    class CarFactory:
        def CarFactory():
            pass
        
        def buildsCar(self, type):
            car = Car()
            location = Location.ASIA

            if location == Location.USA:
                car = Car(USACarFactory.USACarFactory.buildCar(type))
            
            elif location == Location.ASIA:
                car = Car(AsiaCarFactory.AsiaCarFactory.builCar(type))
            
            return car
