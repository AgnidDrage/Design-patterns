import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String args[]) {
        // Crear los elementos
        Guerrero g1 = new Guerrero();
        Guerrero g2 = new Guerrero();
        Mago m1 = new Mago();
        Mago m2 = new Mago();
        // Crear una lista para guardar los elementos
        List<IPersonaje> personajes = new ArrayList<IPersonaje>();
        // Agregar los elementos a una lista
        personajes.add(g1);
        personajes.add(g2);
        personajes.add(m1);
        personajes.add(m2);
        // Creamos el Visitor y le pasamos la lista
        IVisitor visitorArma = new EquiparArma();
        visitorArma.visit( personajes );
        // Comprobar el resultado:
        System.out.println( "Arma del guerrero g1: " + g1.getArma() );
        System.out.println( "Arma del guerrero g2: " + g2.getArma() );
        System.out.println( "Arma del mago m1: " + m1.getArma() );
        System.out.println( "Arma del mago m1: " + m2.getArma() );
    }
}
