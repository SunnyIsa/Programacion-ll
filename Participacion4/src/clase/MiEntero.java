package clase;

public class MiEntero {
	private int valor;
	public MiEntero(int valor){
		this.valor=valor;
	}
	public int get() {
		return valor;
	}
	public boolean esPar() {
		if(this.valor%2==0) {
			return true;
		}else {
			return false;
		}
		
	}
	public boolean esImpar() {
		if(this.valor%2!=0) {
			return true;
		}else {
			return false;
		}
		
	}
	public boolean esPrimo() {
		if (valor <= 1) return false;
        for (int i = 2; i < valor; i++) {
            if (valor % i == 0) return false;
        }
        return true;
		
	}
	public static boolean esPar(int valor) {
		if(valor%2==0) {
			return true;
		}else {
			return false;
		}
		
	}
	public static boolean esImpar(int valor) {
		if(valor%2!=0) {
			return true;
		}else {
			return false;
		}
		
	}
	public static boolean esPrimo(int valor) {
		if (n <= 1) return false;
        for (int i = 2; i < valor; i++) {
            if (valor % i == 0) return false;
        }
        return true;
		
	}
	public static boolean esPar(MiEntero v) {
		return v.getValor() % 2 == 0;
		
	}
	public static boolean esImpar(MiEntero v) {
		return v.getValor() % 2 != 0;
		
	}
	public static boolean esPrimo(MiEntero v) {
	       return v.esPrimo();
		
	}
	public boolean equals(int n) {
		return this.valor==n;
	}
	public boolean equals(MiEntero v) {
		return this.valor==v.get();
	}
	public static int parseInt(char[] array) {
		return Integer.parseInt(new String(array));
	}
	public static int parseInt(String s) {
		return Integer.parseInt(s);
		
	}


}
