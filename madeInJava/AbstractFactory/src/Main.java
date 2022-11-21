import AbstractFactory.ComputerFactory;
import AbstractFactory.PCFactory;
import AbstractFactory.ServerFactory;
import Product.Computer;
import Product.PC;

public class Main {
    public static void main(String args[]){
        Computer pc = ComputerFactory.getComputer(new PCFactory("2 GB","500 GB","2.4 GHz"));
        Computer server = ComputerFactory.getComputer(new ServerFactory("16 GB","1 TB","2.9 GHz"));
        System.out.println("PC: " + pc);
        System.out.println("Server: " + server);
    }
}
