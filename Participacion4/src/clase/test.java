package clase;

public class test {
    public static void main(String[] args) {
        // Crear objetos
        MiEntero a = new MiEntero(7);
        MiEntero b = new MiEntero(10);

        // Métodos de instancia
        System.out.println("a es par? " + a.esPar());
        System.out.println("a es primo? " + a.esPrimo());
        System.out.println("b es impar? " + b.esImpar());

        // Métodos estáticos con int
        System.out.println("¿11 es primo? " + MiEntero.esPrimo(11));

        // Métodos estáticos con objetos
        System.out.println("¿b es par? " + MiEntero.esPar(b));

        // equals
        System.out.println("a.equals(7)? " + a.equals(7));
        System.out.println("a.equals(b)? " + a.equals(b));

        // parseInt
        char[] numeros = {'1', '2', '3', '4'};
        System.out.println("parseInt(char[]) = " + MiEntero.parseInt(numeros));
        System.out.println("parseInt(String) = " + MiEntero.parseInt("5678"));
    }
}