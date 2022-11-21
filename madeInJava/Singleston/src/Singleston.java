public class Singleston {
    static private Singleston singleston = null;

    private Singleston() {
    }

    static public Singleston getSingleston() {
        if (singleston == null) {
            singleston = new Singleston();
        }
        return singleston;
    }

    public void saySomething() {
        System.out.println("Hi, im the only singleston");
    }
}
