import Composite


class SectorCajas(Composite.Composite):
    def __init__(self, cantCajeros):
        self.cantCajeros = cantCajeros

    def getCantCajeros(self):
        return self.cantCajeros