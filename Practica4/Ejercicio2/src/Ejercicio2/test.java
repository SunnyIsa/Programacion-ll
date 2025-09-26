package Ejercicio2;

public class test {

	public static void main(String[] args) {
		String[] colores={"Rojo", "Verde", "Azul", "Amarillo", "Violeta","Naranja","Rosa","Celeste","Negro","Blanco"};
		Figura[] figuras=new Figura[5];
		for(int j = 0; j < figuras.length; j++) {
			int i=(int)(Math.random()*2)+1;
			double l=Math.random()*10+1;
			if (i==1) {
				figuras[j]=new Cuadrado(colores[(int)(l-1)],l);
			}else {
				figuras[j]=new Circulo(colores[(int)(l-1)],l);
			}
			
		}
        for (Figura f : figuras) {
        	if(f instanceof Cuadrado )
        		System.out.printf("Cuadrado: color=%s | área=%.2f | perímetro=%.2f%n",f.getColor(), f.area(), f.perimetro());
        	else if(f instanceof Circulo )
                System.out.printf("Circulo: color=%s | área=%.2f | perímetro=%.2f%n",f.getColor(), f.area(), f.perimetro());
        	if (f instanceof Coloreado) {
                System.out.println("   " + ((Coloreado) f).comoColorear());
            }
        }    

	}

}
