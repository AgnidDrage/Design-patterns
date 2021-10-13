class Libro:
    def __init__(self, titulo, estado):
        self._titulo = titulo
        self._estado = estado

    def getTitulo(self):
        return self._titulo
    
    def setTitulo(self, titulo):
        self._titulo = titulo

    def getEstado(self):
        return self._estado
    
    def setEstado(self, estado):
        self._estado = estado
    
    