public class MiClase {
    public int suma(int a, int b, int c) {
        return a + b + c;
    }
    public static void main(String[] args) {
        MiClase miObjeto = new MiClase();
        int resultado = miObjeto.suma(5, 4, 3);
        System.out.println(resultado);
    }
}