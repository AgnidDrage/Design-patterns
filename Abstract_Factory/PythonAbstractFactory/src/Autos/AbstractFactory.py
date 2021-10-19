from CarFactory import CarFactory
from CarType import CarType


class AbstractFactory:
    def __init__(self):
        print(CarFactory().buildsCar(type=CarType.SMALL))
        print(CarFactory().buildsCar(type=CarType.LUXURY))


if __name__ == '__main__':
    AbstractFactory()