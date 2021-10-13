from subject import Subject


class AlarmaLibro(Subject):
    def __init__(self):
        self._observadores = []
    
    def attach(self, unObserver):
        self._observadores.append(unObserver)
    
    def detach(self, unObserver):
        self._observadores.remove(unObserver)

    def notifyObserver(self):
        for i in self._observadores:
            i.update()