package Factory;

import Product.Equilatero;
import Product.Triangulo;

public class EquilateroFactory implements FactoryMethod{

    public EquilateroFactory() {
    }

    public Equilatero createTriangulo(int _ladoA, int _ladoB, int _ladoC) {
        return new Equilatero(_ladoA, _ladoB, _ladoC);
    }
}
