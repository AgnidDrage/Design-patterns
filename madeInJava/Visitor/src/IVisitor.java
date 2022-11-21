import java.util.List;

public interface IVisitor {
    public void visit(Guerrero g);
    public void visit(Mago m);
    public void visit(List<IPersonaje> elementList);
}
