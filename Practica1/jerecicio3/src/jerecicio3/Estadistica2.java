package jerecicio3;

public class Estadistica2 {
	private float[] vars;
	public Estadistica2(float[] vars) {
		this.vars= vars;
	}
	public float promedio() {
		float suma = 0f;
		for (int i=0;i<10;i++) {
			suma+= vars[i];
			
		}
		return suma/10;
	}
	public float desviacion() {
		float prom=promedio();
		float des=0f;
		for(int i=0;i<10;i++) {
			des+=((vars[i]-prom)*(vars[i]-prom))/9;
		}
		return (float)Math.sqrt(des);	
	}
}
