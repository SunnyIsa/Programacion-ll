package Ejercicio1;

public class test {

	public static void main(String[] args) {
		Empleado e1=new EmpleadoTiempoCompleto("Juan",25000);
		Empleado e2=new EmpleadoTiempoCompleto("Esteve",27750);
		Empleado e3=new EmpleadoTiempoCompleto("Loren",30570);
		Empleado e4=new EmpleadoTiempoHorario("Glora",130,60);
		Empleado e5=new EmpleadoTiempoHorario("Alex",160,30);
		Empleado[] empleados= {e1,e2,e3,e4,e5} ;
		for (Empleado e:empleados) {
			System.out.println("Nombre: "+e.nombre+"| Salario Mensual: "+e.CalcularSalarioMensual());
		}
	}

}
