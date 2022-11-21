package Factory;

import Product.Triangulo;

import java.util.Optional;

public interface FactoryMethod {
    Triangulo createTriangulo(int _ladoA, int _ladoB, int _ladoC);
}
