package composicion;
import java.util.ArrayList;
public class Empresa {
	private String nombre;
	public ArrayList<Empleado> empleados;
	public ArrayList<String> empsCon;
	public Empresa(String nombre) {
		this.nombre = nombre;
		this.empleados = new ArrayList<Empleado>();
		this.empsCon = new ArrayList<>();
		
		
	}
	public void contratar(Empleado emp) {
		empleados.add(emp);
	}
	
	public String getNombre() {
		return nombre;
	}


	public void listar_empleados() {
		System.out.println(empleados);
		
	}
	
	
	
}
