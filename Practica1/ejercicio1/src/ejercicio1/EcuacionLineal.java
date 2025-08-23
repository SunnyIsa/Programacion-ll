package ejercicio1;

public class EcuacionLineal {
	private double a;
	private double b;
	private double c;
	private double d;
	private double e;
	private double f;
	EcuacionLineal(double a,double b,double c,double d,double e,double f){
		this.a=a;
		this.b=b;
		this.c=c;
		this.d=d;
		this.e=e;
		this.f=f;
	}
	public boolean tieneSolucion(){
		if(a*d-b*c==0) {
			return false;
		}
		else{
			return true;
		}
		
	}
	public double getX() {
		return (e * d - b * f) / (a * d - b * c);
	}
	public double getY() {
		return (a * f - e * c) / (a * d - b * c);
	}
	}
	
	


