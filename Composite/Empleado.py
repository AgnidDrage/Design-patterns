import ISueldo


class Empleado(ISueldo.ISueldo):
    def __init__(self, nombreCompleto, cargo, sueldo):
        self.nombreCompleto = nombreCompleto
        self.cargo = cargo
        self.sueldo = sueldo

    def Empleado(self):
        pass

    def Empleado(self, nombreCompleto, cargo, sueldo):
        self.nombreCompleto = nombreCompleto
        self.cargo = cargo
        self.sueldo = sueldo
    
    def getSueldo(self):
        return 0