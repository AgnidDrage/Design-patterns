package Factory;

import Product.Escaleno;
import Product.Triangulo;

public class EscalenoFactory implements FactoryMethod{

    public EscalenoFactory() {
    }

    public Escaleno createTriangulo(int _ladoA, int _ladoB, int _ladoC) {
        return new Escaleno(_ladoA, _ladoB, _ladoC);
    }
}
