package Ejercicio1;

public class EmpleadoTiempoCompleto extends Empleado{
	private double salario_anual;

	public EmpleadoTiempoCompleto(String nombre,double salario_anual) {
		super(nombre);
		this.salario_anual = salario_anual;
	}

	@Override
	public double CalcularSalarioMensual() {
		return this.salario_anual/12;
	}

	@Override
	public String toString() {
		return "EmpleadoTiempoCompleto [salario_anual=" + salario_anual + "]";
	}
	
	
}
