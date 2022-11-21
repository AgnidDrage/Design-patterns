public abstract class Logger {
    public static int ERR = 3;
    public static int NOTICE = 5;
    public static int DEBUG = 7;
    protected int mask;

    protected Logger next;

    public Logger setNext(Logger l) {
        next = l;
        return this;
    }

    abstract public void message(String msg, int priority);
}
