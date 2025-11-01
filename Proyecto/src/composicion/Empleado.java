package composicion;

public class Empleado {
	private String nombre;
	private String puesto;
	private Direccion direccion;
	public Empleado(String n, String p, String cDir, String dDir,int nDir) {
		this.nombre = n;
		this.puesto = p;
		this.direccion =new Direccion(cDir,dDir,nDir);
	}
	
	public String getNombre() {
		return nombre;
	}

	public String getPuesto() {
		return puesto;
	}

	public Direccion getDireccion() {
		return direccion;
	}



	@Override
	public String toString() {
		return "Empleado [nombre=" + nombre + ", puesto=" + puesto + ", direccion=" + direccion + "]";
	}
	

	
	
	
}
