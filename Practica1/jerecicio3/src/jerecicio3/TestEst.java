package jerecicio3;

import java.util.Scanner;

public class TestEst {

	public static void main(String[] args) {
		Scanner scanner= new Scanner(System.in);
		float[] vars=new float[10];
		System.out.println("Ingresa las 10 variables");
		for(int i=0;i<10;i++) {
			vars[i]=scanner.nextFloat();
		}
		Estadistica2 estadistica= new Estadistica2(vars);
		System.out.println("El promedio es "+ estadistica.promedio());
		System.out.println("La desviacion estandard es "+ estadistica.desviacion());

	}

}
