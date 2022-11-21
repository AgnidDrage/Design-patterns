package Factory;

import Product.Isosceles;
import Product.Triangulo;

public class IsoscelesFactory implements FactoryMethod{

    public IsoscelesFactory() {
    }

    public Isosceles createTriangulo(int _ladoA, int _ladoB, int _ladoC) {
        return new Isosceles(_ladoA, _ladoB, _ladoC);
    }
}
