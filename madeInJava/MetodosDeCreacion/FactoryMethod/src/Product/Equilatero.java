package Product;

public class Equilatero extends Triangulo{

    public Equilatero(int _ladoA, int _ladoB, int _ladoC) {
        ladoA = _ladoA;
        ladoB = _ladoB;
        ladoC = _ladoC;
    }

    @Override
    public String getDescripcion() {
        return "Es un triangulo equilatero";
    }
}
