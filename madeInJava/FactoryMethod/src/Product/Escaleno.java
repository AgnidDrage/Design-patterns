package Product;

public class Escaleno extends Triangulo{

    public Escaleno(int _ladoA, int _ladoB, int _ladoC) {
        ladoA = _ladoA;
        ladoB = _ladoB;
        ladoC = _ladoC;
    }

    public String getDescripcion() {
        return "Es un triangulo escaleno";
    }
}
