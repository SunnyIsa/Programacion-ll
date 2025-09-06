package ejercicio1;

public class test {

	public static void main(String[] args) {
		double[] a= {1,2,-1};
		double[] b= {2,-1,0};
		int[] c= {2,3};
		int[] d= {4,6};
		if(a.length==b.length) {
			//usar String,int,double o boolean para escoger lla formula de perpendicular
			AlgebraVectorial vects= new AlgebraVectorial(a,b);
			AlgebraVectorial vects2= new AlgebraVectorial(c,d);
			System.out.println("a y b son perpendiculares? "+vects.Perpendicular("hola"));
			System.out.println("a y b son mutuamente ortogonales? "+vects2.Perpendicular(6));
			System.out.println("a y b son perpendiculares? "+vects.Perpendicular(5.0));
			System.out.println("a y b son paralelos? "+vects2.Paralela());
			System.out.println("a y b son paralelos? "+vects.Paralela());
			System.out.println("la proyeccion de a sobre b es:  ");
			AlgebraVectorial.imprimirVector(vects2.proy());
			System.out.println("la componente de a sobre b es:  " + vects2.comp());
			

			
			
		}else {
			System.out.println("los vectores deben tener la misma cantidad de elementos");
		}


	}

}
