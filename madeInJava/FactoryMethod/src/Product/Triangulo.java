package Product;

public abstract class Triangulo {
    int ladoA;
    int ladoB;
    int ladoC;


    public String getDescripcion(){
        return "Es un triangulo";
    };

    public String getLados(){
        return "ladoA: " + ladoA + " ladoB: " + ladoB + " ladoC: " + ladoC;
    }
}
