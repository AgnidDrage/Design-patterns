from iLibroMalEstado import ILibroMalEstado


class Compras(ILibroMalEstado):
    def update(self):
        print("Compras:");
        print("Solicito cotización de reparación o reposición de libro...");