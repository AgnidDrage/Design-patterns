public class Client {
    public static void main(String args[]) {
        Composite raiz = new Composite("root");
        raiz.agregar(new Hoja("HojaA"));
        raiz.agregar(new Hoja("HojaB"));
        Composite comp = new Composite("Compuesto X");
        comp.agregar(new Hoja("HojaXA"));
        comp.agregar(new Hoja("HojaXB"));
        raiz.agregar(comp);
        raiz.agregar(new Hoja("HojaC"));
        Hoja l = new Hoja("HojaD");
        raiz.agregar(l);
        raiz.remover(l);
        raiz.mostrar(1);
    }
}
