package jerecicio3;
import java.util.Scanner;
public class Estadistica1 {

	public static void main(String[] args) {
		float[] vars= new float[10];
		Scanner scanner= new Scanner(System.in);
		System.out.println("Ingresa las 10 variables");
		for(int i=0;i<10;i++) {
			vars[i]=scanner.nextFloat();
		}
		System.out.println("El promedio es "+promedio(vars));
		System.out.println("La desviacion estandard es "+desviacion(vars));

			
		}
	public static float promedio(float[] A) {
		float suma = 0f;
		for (int i=0;i<10;i++) {
			suma+= A[i];
			
		}
		return suma/10;
	}
	public static float desviacion(float[] A) {
		float prom=promedio(A);
		float des=0f;
		for(int i=0;i<10;i++) {
			des+=((A[i]-prom)*(A[i]-prom))/9;
		}
		return (float)Math.sqrt(des);		
	}
	

	}


