package ejercicio2;

public class Vector {
	private double x;
	private double y;
	private double z;
	public Vector() {
		this.x= 0;
		this.y= 0;
		this.z= 0;
	}
	public Vector(double[] c) {
		this.x= c[0];
		this.y= c[1];
		this.z= c[2];
	}
	public Vector(double x,double y, double z) {
		this.x= x;
		this.y= y;
		this.z= z;
	}
	public Vector suma(Vector v) {
		return new Vector(this.x+v.x,this.y+v.y,this.z+v.z);
	}
	public Vector suma(double a, double b, double c) { 
			return new Vector(x+a, y+b, z+c); 
	}
	public Vector resta(Vector v) {
		return new Vector(this.x-v.x,this.y-v.y,this.z-v.z);
	}
	public Vector resta(double a, double b, double c) { 
			return new Vector(this.x-a, this.y-b,this.z-c); 
	}
	public Vector MultEsc(double s) {
		return new Vector(this.x*s,this.y*s,this.y*s);
	}
	public double mod() {
		return(Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z));
	}
	public Vector norm() {
		return new Vector(this.x/mod(),this.y/mod(),this.z/mod());
	}
	public double ProdEsc(Vector v) {
		return this.x*v.x+this.y*v.y+this.z*v.z;
	}
	public Vector ProdVect(Vector v) {
		return new Vector(this.y*v.z-this.z*v.y,this.z*v.x-this.x*v.z,this.x*v.y-this.y*v.x);
	}
	public Vector proy(Vector v) {
		double s=ProdEsc(v)/v.mod();
		return new Vector(s*v.x,s*v.y,s*v.z);
	}
	public double comp(Vector v) {
		return ProdEsc(v)/v.mod();
	}
	public boolean Perpendicular(Vector v) {
		return suma(v).mod()==resta(v).mod();
	}
	public String toString() {
	    return String.format("[%f, %f, %f]", this.x, this.y, this.z);
	}
	
	
	
}
