package ejercicio1;

public class AlgebraVectorial {
	private double[] a;
	private double[] b;

	public AlgebraVectorial(double[] a,double[] b){
		this.a=a;
		this.b=b;
	}
	public AlgebraVectorial(int[] a,int[] b){
		double [] ad=new double[a.length];
		double [] bc=new double[a.length];
		for (int i=0;i<a.length;i++) {
			ad[i]=a[i];
			bc[i]=b[i];
		}
		this.a=ad;
		this.b=bc;
	}
	public AlgebraVectorial(double[] a,int[] b){
		double [] bc=new double[a.length];
		for (int i=0;i<a.length;i++) {
			bc[i]=b[i];
		}
		this.b=bc;
	}
	public AlgebraVectorial(int[] a,double[] b){
		double [] ad=new double[a.length];
		for (int i=0;i<a.length;i++) {
			ad[i]=a[i];
		}
		this.a=ad;

	}
	public double[] suma() {
		double[] r= new double[this.a.length];
		for(int i=0;i<this.a.length;i++) {
			r[i]=(double) (this.a[i]+this.b[i]);
			
		}
		return r;
	}
	public double[] resta() {
		double[] r= new double[this.a.length];
		for(int i=0;i<this.a.length;i++) {
			r[i]=(double) (this.a[i]-this.b[i]);
			
		}
		return r;
	}
	public double[] restainv() {
		double[] r= new double[this.a.length];
		for(int i=0;i<this.a.length;i++) {
			r[i]=(double) (this.b[i]-this.a[i]);
			
		}
		return r;
	}
	public double mod(double[] x) {
		double suma=0;
		for (int i=0;i<x.length;i++) {
			suma+=x[i]*x[i];
		}
		return Math.sqrt(suma);
	}
	public double prodpun() {
		double suma=0;
		for (int i = 0;i<this.a.length;i++) {
			suma+=this.a[i]*this.b[i];
		}
		return suma;	
	}
	public double mod2(double[] x) {
		double suma=0;
		for (int i=0;i<x.length;i++) {
			suma+=x[i]*x[i];
		}
		return suma;
	}
	public boolean Perpendicular(String x) {
		return mod(suma())==mod(resta());
		}
	public boolean Perpendicular(int y) {
		return mod(resta())==mod(restainv());
		
	}
	public boolean Perpendicular(double z) {
		return prodpun()==0;
		
	}
	public boolean Perpendicular(boolean w) {
		return mod2(suma())==((mod(this.a)*mod(this.a)))+((mod(this.b)*mod(this.b)));
	}
	public boolean Paralela(){
		if (this.a.length==3) {
	        double x = a[1]*b[2] - a[2]*b[1];
	        double y = a[2]*b[0] - a[0]*b[2];
	        double z = a[0]*b[1] - a[1]*b[0];
	        return x == 0 && y == 0 && z == 0;
		}
		else {
		    double r = 0.0;
		    for (int i=0;i<this.a.length;i++) {
		        if (this.b[i]!=0) {
		            double k = this.a[i]/this.b[i]; 
		            if (r==0.0) {
		                r=k; 
		            } else if (k!=r) {
		                return false;  
		            }
		        } else if (this.a[i]!=0) {
		            return false;  
		        }
		    }
		    return true;	
		}

	}
	public double[] proy() {
		double[] r= new double[a.length];
		double s=prodpun()/mod2(b);
		for(int i=0;i<a.length;i++) {
			r[i]=b[i]*s;
		}
		return r;	
	}
	public double comp() {
		return prodpun()/mod(b);	
	}
	public static void imprimirVector(double[] v) {
		System.out.print("[ ");
	    for (int i = 0; i < v.length; i++) {
	        System.out.print(v[i] + " ");
	    }
	    System.out.println("]");
	}
}
