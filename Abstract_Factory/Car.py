

class Car:
    def __init__(self, model=None, location=None):
        self.model = model
        self.location = location
    
    def construct(self):
        pass

    def getModel(self):
        return self.model

    def getLocation(self):
        return self.location

    def setModel(self, model):
        self.model = model
    
    def setLocation(self, location):
        self.location = location
    
    def __str__(self) -> str:
        return "Model - " + self.model + " built in " + self.location