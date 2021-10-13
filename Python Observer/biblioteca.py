from libro import Libro
from alarmaLibro import AlarmaLibro


class Biblioteca:
    def devuelveLibro(self, libro, alarma):
        if libro.getEstado() == "MALO":
            alarma.notifyObserver()