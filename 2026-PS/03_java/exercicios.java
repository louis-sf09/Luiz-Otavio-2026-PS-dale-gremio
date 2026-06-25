public class exercicios {

    // Método Problema 1
    static double calcularDesconto(double valor, double percentual) {
        System.out.println(valor-(valor*percentual));
        return valor-(valor*percentual);
    }

    // Método Problema 2
    static int maiorNumero(int a, int b) {
        if (a > b) {
            System.out.println(a);
            return a;
        } else {
            System.out.println(b);
            return b;
        }
    }

    // Método Problema 3
    static double calcularFrete(double peso) {
        if (peso <= 1) {
            System.out.println("R$10,00");
            return 10;
        } else if (peso <= 5) {
            System.out.println("R$20,00");
            return 20;
        } else {
            System.out.println("R$35,00");
            return 35;
        }
    }

    // Métodos Problema 4
    static int somar(int a, int b) {
        System.out.println(a+b);
        return a+b;
    }

    static double somar(double a, double b) {
        System.out.println(a+b);
        return a+b;
    }

    // Métodos Problema 5
    static void exibirProduto(String nome) {
        System.out.println("Produto: " + nome);
    }

    static void exibirProduto(String nome, double preco) {
        System.out.println("Produto: " + nome + "\nPreço: R$ " + preco);
    }

    public static void main(String[] args) {
        // Testes Problema 1
        System.out.println();
        calcularDesconto(100, 0.10);
        calcularDesconto(250, 0.20);
        calcularDesconto(500, 0.15);

        // Testes Problema 2
        System.out.println();
        maiorNumero(10, 20);
        maiorNumero(50, 5);
        maiorNumero(30, 30);

        // Testes Problema 3
        System.out.println();
        calcularFrete(0.5);
        calcularFrete(3);
        calcularFrete(8);

        // Testes Problema 4
        System.out.println();
        somar(5,3);
        somar(2.5, 3.5);
        somar(100, 50);

        // Testes Problema 5
        System.out.println();
        exibirProduto("Refrigerante");
        exibirProduto("Pizza", 39.90);
        exibirProduto("Hambúrguer",22.50);
    }
}
