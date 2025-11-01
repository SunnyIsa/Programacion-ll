package composicion;

import java.util.ArrayList;

import Vistas.Datos;

public class Aplicacion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Empleado e1=new Empleado("Juan","Gerente","La Paz","San Pedro",123);
		Empleado e2=new Empleado("Maria","Gerente","La Paz","Sopocachi",456);
		Empresa em1=new Empresa("ABC");
		Datos.empsNoms.add(e1.getNombre());
		System.out.println(e1);
		em1.contratar(e1);
		em1.contratar(e2);
		em1.listar_empleados();
		
	}

}
