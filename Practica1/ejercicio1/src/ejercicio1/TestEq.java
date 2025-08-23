package ejercicio1;
import java.util.Scanner;
public class TestEq {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		System.out.println("Ingresa a,b,c,d.e.f:");
		double a=scanner.nextDouble();
		double b=scanner.nextDouble();
		double c=scanner.nextDouble();
		double d=scanner.nextDouble();
		double e=scanner.nextDouble();
		double f=scanner.nextDouble();
		EcuacionLineal ecuacion=new EcuacionLineal(a,b,c,d,e,f);
		if(ecuacion.tieneSolucion()) {
			System.out.println("x = "+ ecuacion.getX() + " y = "+ecuacion.getY());
		}
		else {
			System.out.println("La ecuacion no tiene solucion");
		}
		

	}

}
