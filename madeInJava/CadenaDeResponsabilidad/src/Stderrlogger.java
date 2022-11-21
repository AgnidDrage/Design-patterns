public class Stderrlogger extends Logger{
    public Stderrlogger(int mask){
        this.mask = mask;
    }

    public void message(String msg, int priority){
        if (priority <= mask) System.out.println("Escribiendo en STDERR: " + msg);
        if (next != null) next.message(msg, priority);
    }
}
