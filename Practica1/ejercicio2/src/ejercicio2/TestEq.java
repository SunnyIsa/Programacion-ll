package ejercicio2;
import java.util.Scanner;
public class TestEq{
    public static void main(String[] args) {
        Scanner input= new Scanner(System.in);
        System.out.println("ingresa a,b y c:");
        double a=input.nextDouble();
        double b=input.nextDouble();
        double c=input.nextDouble();
    EcuacionLineal ecuacion= new EcuacionLineal(a,b,c);
    if(ecuacion.getDiscriminante()>0) {
    	System.out.println("La ecuacion tiene dos raices"+ecuacion.getRaiz1()+" y "+ecuacion.getRaiz2());
    	} else if(ecuacion.getDiscriminante()==0){
    		System.out.println("La ecuacion tiene una raiz "+ecuacion.getRaiz1());
    	}else{
    			System.out.println("La ecuacion no tiene raices reales");
}}}