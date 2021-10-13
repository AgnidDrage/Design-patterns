from biblioteca import Biblioteca
from alarmaLibro import AlarmaLibro
from compras import Compras
from administracion import Administracion
from stock import Stock
from libro import Libro



def main():
    sujetoConcreto = AlarmaLibro()
    observerCompras = Compras()
    observerAdministracion = Administracion()
    observerStock = Stock()

    sujetoConcreto.attach(observerCompras)
    sujetoConcreto.attach(observerAdministracion)
    sujetoConcreto.attach(observerStock)

    unLibro = Libro('Caperucita', 'MALO')

    biblioteca = Biblioteca()

    biblioteca.devuelveLibro(unLibro, sujetoConcreto)

if __name__=='__main__':
    main()