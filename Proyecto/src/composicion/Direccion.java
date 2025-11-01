package composicion;

public class Direccion {
	private String ciudad;
	private String direccion;
	private int numero;
	public Direccion(String ci, String d, int n) {
		this.ciudad = ciudad;
		this.direccion = direccion;
		this.numero = numero;
	}
	@Override
	public String toString() {
		return "Direccion [ciudad=" + ciudad + ", direccion=" + direccion + ", numero=" + numero + "]";
	}
	
	
}
