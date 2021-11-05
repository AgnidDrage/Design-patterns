import IAprobador


class Director(IAprobador.IAprobador):


    def getNext(self):
        return self.next
        
    def solicitudPrestamo(self, monto):
        if monto > 100000:
            print('Lo manejo yo, el Director')
        else:
            self.next.solicitudPrestamo(monto)
    
    def setNext(self, aprobador):
        self.next = aprobador