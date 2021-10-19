from Car import Car
from Location import Location
from USACarFactory import USACarFactory
from AsiaCarFactory import AsiaCarFactory



class CarFactory:
    def CarFactory():
        pass

    def buildsCar(self, type):
        car = Car()
        location = Location.ASIA

        if location == Location.USA:
            car = USACarFactory().buildCar(model=type)
        
        if location == Location.ASIA:
            car = AsiaCarFactory().buildCar(model=type)

        return car