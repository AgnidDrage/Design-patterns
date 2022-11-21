public class EjemploCadenaResponsabilidad {
    public static void main(String args[]) {
        // Construimos la cadena
        // DebugLogger(DEBUG = 7) => EMailLogger(Error = 3) => StderrLogger(Notice = 5)
        Logger l = new DebugLogger(Logger.DEBUG).setNext(new EmailLogger(Logger.ERR).setNext(new Stderrlogger(Logger.NOTICE)));

        // Ejecutamos
        l.message("Entrando en funcion y.", Logger.DEBUG);
        l.message("paso 1 completado.", Logger.NOTICE);
    }
}
