package Ejercicio2;

public class Cuadrado extends Figura implements Coloreado {
	private double lado;
	
	public Cuadrado(String color,double lado) {
		super(color);
		this.lado = lado;
	}

	@Override
	public String comoColorear() {
		return "Colorear los cuatro lados";
	}

	@Override
	public double area() {
		return this.lado*this.lado;
	}

	@Override
	public double perimetro() {
		return this.lado*4;
	}
	

}
