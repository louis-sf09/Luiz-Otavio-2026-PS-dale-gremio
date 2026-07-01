import java.util.Scanner;
import java.util.ArrayList;

public class aula29 {
    
    // ================= 1 =================
    static double calcularMedia(double[] notas) {
        double media = 0;
        for (int i=0; i<notas.length; i++) {
            media += notas[i];
        }
        media /= notas.length;
        return media;
    }

    // ================= 2 =================
    static int contarAprovados(double[] notas) {
        int acima = 0;
        for (int i=0; i<notas.length; i++) {
            if (notas[i] >= 6.0) {
                acima ++;
            }
        }
        return acima;
    }

    // ================= 3 =================
    static void adicionarProduto(ArrayList<String> lista, String nome) {
        lista.add(nome);
    }

    static void listarProdutos(ArrayList<String> lista) {
        for (int i=0; i<lista.size(); i++) {
            System.out.println((i+1) + " - " + lista.get(i));
        }
    }

    // ================= 4 =================
    static int maiorValor(int[] valores) {
        int maior = valores[0];
        for (int i=0; i<valores.length; i++){
            if (valores[i] > maior) {
                maior = valores[i];
            }
        }
        return maior;
    }

    static int maiorValor(int a, int b) {
        if (a>=b) {
            return a;
        } else {
            return b;
        }
    }

    // ================= 5 =================
    static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprov = contarAprovados(notas);
        System.out.println("\nMédia: " + media);
        System.out.println("Aprovados: " + aprov);
        if (media >= 6.0) {
            System.out.println("Situação: APROVADA");
        } else {
            System.out.println("Situação: EM RECUPERAÇÃO");
        }
    }

    public static void main(String[] args) {

        // ================= Testes 1, 2 e 5 =================
        Scanner entrada = new Scanner(System.in);

        System.out.print("Quantidade de notas da lista: ");
        int qtd = entrada.nextInt();

        double[] notas = new double[qtd];
        double elemento = 0;

        for (int i=0; i<qtd; i++) {
            System.out.print("Nota " + (i+1) + ": ");
            elemento = entrada.nextDouble();
            notas[i] = elemento;
        }

        exibirBoletim(notas);

        // ================= Testes 3 =================
        ArrayList<String> lista = new ArrayList<>();

        entrada.nextLine();

        System.out.print("\n1° Produto para acionar: ");
        String nome = entrada.nextLine();
        adicionarProduto(lista, nome);

        System.out.print("\n2° Produto para acionar: ");
        nome = entrada.nextLine();
        adicionarProduto(lista, nome);

        System.out.println("\n--- Lista de Produtos ---");
        listarProdutos(lista);

        // ================= Testes 4 =================
        System.out.println("\nMaior (3, 9, 5): " + maiorValor(new int[]{3, 9, 5}));
        System.out.println("Maior (12, 7): " + maiorValor(12, 7));
        System.out.println("Maior (4, 4, 4): " + maiorValor(new int[]{4, 4, 4}));

    }
}
