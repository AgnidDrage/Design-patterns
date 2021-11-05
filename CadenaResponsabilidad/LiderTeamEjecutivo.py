import IAprobador


class LiderTeamEjecutivo(IAprobador.IAprobador):
    def getNext(self):
        return self.next

    def solicitudPrestamo(self, monto):
        if monto > 10000 and monto <= 50000:
            print('Lo manejo yo, el Lider')
        else:
            self.next.solicitudPrestamo(monto)
        
    def setNext(self, aprobador):
        self.next = aprobador