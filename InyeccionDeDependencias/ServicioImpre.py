class ServicioImpre:
    def __init__(self, servicioA, servicioB):
        self.servicioA = servicioA
        self.servicioB = servicioB

    def getServicioB(self):
        return self.servicioB
    
    def getServicioA(self):
        return self.servicioA
    
    def setServicioB(self, servicioB):
        self.servicioB = servicioB

    def setServicioA(self, servicioA):
        self.servicioA = servicioA

    def ServicioImpre(self, servicioA, servicioB):
        self.servicioA = servicioA
        self.servicioB = servicioB

    def imprimir(self):
        self.servicioA.enviar()
        self.servicioB.pdf()