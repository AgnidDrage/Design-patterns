import IAprobador
from EjecutivoCuenta import EjecutivoCuenta
from LiderTeamEjecutivo import LiderTeamEjecutivo
from Gerente import Gerente
from Director import Director

class Banco(IAprobador.IAprobador):
    
    def getNext(self):
        return self.next
    
    def solicitudPrestamo(self, monto):
        ejecutivo = EjecutivoCuenta()
        self.setNext(ejecutivo)

        lider = LiderTeamEjecutivo()
        ejecutivo.setNext(lider)

        gerente = Gerente()
        lider.setNext(gerente)

        director = Director()
        gerente.setNext(director)

        self.next.solicitudPrestamo(monto)
    
    def setNext(self, aprobador):
        self.next = aprobador