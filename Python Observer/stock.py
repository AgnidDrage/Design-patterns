from iLibroMalEstado import ILibroMalEstado


class Stock(ILibroMalEstado):
    def update(self):
        print("Stock:")
        print("Se da de baja al libro y se manda a reparación o reposición...")