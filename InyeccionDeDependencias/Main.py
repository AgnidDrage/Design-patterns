from ServicioEnvio1 import ServicioEnvio1
from ServicioImpre import ServicioImpre
from ServicioPDF import ServicioPDF1


def main():
    servi1 = ServicioEnvio1()
    servi2 = ServicioPDF1()
    miServi = ServicioImpre(servi1, servi2)

    miServi.imprimir()

if __name__ == '__main__':
    main()