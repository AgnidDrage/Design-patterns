package Product;

public class Isosceles extends Triangulo{

    public Isosceles(int _ladoA, int _ladoB, int _ladoC) {
        ladoA = _ladoA;
        ladoB = _ladoB;
        ladoC = _ladoC;
    }

    public String getDescripcion() {
        return "Es un triangulo Isosceles";
    }

}
