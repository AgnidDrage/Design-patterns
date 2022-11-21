import Factory.EquilateroFactory;
import Factory.EscalenoFactory;
import Factory.FactoryMethod;
import Factory.IsoscelesFactory;
import Product.Equilatero;
import Product.Escaleno;
import Product.Isosceles;

public class Main {
    public static void main(String args[]) {
        EquilateroFactory equilateroFactory = new EquilateroFactory();
        IsoscelesFactory isoscelesFactory = new IsoscelesFactory();
        EscalenoFactory escalenoFactory = new EscalenoFactory();

        Isosceles isosceles = isoscelesFactory.createTriangulo(3, 3, 2);
        Equilatero equilatero = equilateroFactory.createTriangulo(3, 3, 3);
        Escaleno escaleno = escalenoFactory.createTriangulo(2, 3, 4);

        System.out.println(isosceles.getDescripcion());
        System.out.println(isosceles.getLados());
        System.out.println(equilatero.getDescripcion());
        System.out.println(equilatero.getLados());
        System.out.println(escaleno.getDescripcion());
        System.out.println(escaleno.getLados());

    }
}
