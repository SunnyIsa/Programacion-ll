package ejercicio2;

public class test {

	public static void main(String[] args) {
		Vector a= new Vector(2,3,4);
		Vector b= new Vector(0,4,-3);
		System.out.println("a+b= "+a.suma(b));
		System.out.println("a-b= "+a.resta(b));
		System.out.println("2*a= "+a.MultEsc(2));
		System.out.println("|a|= "+a.mod());
		System.out.println("La normal de a es : "+a.norm());
		System.out.println("a*b= "+a.ProdEsc(b));
		System.out.println("axb= "+a.ProdVect(b));
		System.out.println("Los vectores son perpendiculares? "+a.Perpendicular(b));
		System.out.println("La proyeccion a sobre b "+a.proy(b));
		System.out.println("El compononte de aa sobre b "+a.comp(b));
		
		

	}

}
