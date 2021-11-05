import ISueldo



class Composite(ISueldo.ISueldo):
    def __init__(self, empleados):
        self.empleados = list(empleados)

    def getsuelo(self):
        for i in range(len(self.empleados)):
            sumador = sumador + self.empleados[i].getSueldo()
        
    
    def agregar(self, p):
        self.empleados.append(p)