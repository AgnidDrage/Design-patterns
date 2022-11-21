public class DebugLogger extends Logger{

    public DebugLogger(int mask) {
        this.mask = mask;
    }

    public void message(String msg, int priority) {
        if (priority<=mask) System.out.println("Escribiendo en DEBUG: " + msg);
        if (next != null) next.message(msg, priority);
    }
}
