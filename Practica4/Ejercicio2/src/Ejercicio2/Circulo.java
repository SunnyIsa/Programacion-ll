package Ejercicio2;

public class Circulo extends Figura{
	private double radio;

	public Circulo(String color, double radio) {
		super(color);
		this.radio = radio;
	}

	@Override
	public double area() {
		return Math.PI*this.radio*this.radio;
	}

	@Override
	public double perimetro() {
		return 2*Math.PI*this.radio;
	}

	
}
