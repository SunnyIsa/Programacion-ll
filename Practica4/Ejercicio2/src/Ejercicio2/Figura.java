package Ejercicio2;

public abstract class Figura {
	public String color;
	

	public Figura(String color) {
		this.color = color;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}
	public abstract double area();
	public abstract double perimetro();

	@Override
	public String toString() {
		return "Figura [color=" + color + "]";
	}
	

}
