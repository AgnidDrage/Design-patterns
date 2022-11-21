import java.util.ArrayList;

public class Composite extends Componente{
    private ArrayList<Componente> hijo = new ArrayList();

    public Composite(String name) {
        super(name);
    }

    public void agregar(Componente componente) {
        hijo.add(componente);
    }

    public void remover(Componente componente) {
        hijo.remove(componente);
    }

    public void mostrar(int profundidad) {
        System.out.println(nombre + " nivel: " + profundidad);
        for (int i=0; i<hijo.size(); i++) {
            hijo.get(i).mostrar(profundidad + 1);
        }
    }
}
