import IAprobador


class EjecutivoCuenta(IAprobador.IAprobador):


    def getNext(self):
        return self.next
    
    def solicitudPrestamo(self, monto):
        if monto <= 10000:
            print('Lo manejo yo, el Ejecutivo de Cuenta')
        else:
            self.next.solicitudPrestamo(monto)
    
    def setNext(self, aprobador):
        self.next = aprobador