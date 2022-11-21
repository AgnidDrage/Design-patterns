public class EmailLogger extends Logger{
    public EmailLogger(int mask){
        this.mask = mask;
    }

    public void message(String msg, int priority){
        if (priority <= mask) System.out.println("Enviando un email: " + msg);
        if (next != null) next.message(msg, priority);
    }
}
