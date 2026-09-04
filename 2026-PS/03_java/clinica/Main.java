import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner teclado = new Scanner(System.in);
    static ArrayList<Produto> produtos = new ArrayList<>();


    static Produto buscarPorCodigo(int codigo) {
        for (int i=0; i<produtos.size(); i++) {
            Produto p = produtos.get(i);
            if (p.getCodigo() == codigo) {
                return p;
            }
        }
        return null;
    }

    public static void main(String[] args) {

        int opcao = 0;

        while (opcao != 5) {

            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Alterar preço");
            System.out.println("4 - Remover");
            System.out.println("5 - Sair");
            System.out.print("Opção: ");

            opcao = teclado.nextInt();
            teclado.nextLine();

            if (opcao == 1) {

                System.out.print("Código: ");
                int codigo = teclado.nextInt();
                teclado.nextLine();

                System.out.print("Nome: ");
                String nome = teclado.nextLine();

                System.out.print("Preço: ");
                double preco = teclado.nextDouble();

                Produto p = new Produto(codigo, nome, preco);
                produtos.add(p);

            } else if (opcao == 2) {

                for (Produto p : produtos) {
                    System.out.println(
                        p.getCodigo() + " - " +
                        p.getNome() + " - R$ " +
                        p.getPreco()
                    );
                }

            } else if (opcao == 3) {

                System.out.print("Código: ");
                int codigo = teclado.nextInt();

                Produto p = buscarPorCodigo(codigo);
                if (p == null) {
                    System.out.println("Nenhum produto encontrado com o código: " + codigo);
                    return;
                }

                System.out.print("Novo preço: ");
                double preco = teclado.nextDouble();

                p.setPreco(preco);

            } else if (opcao == 4) {

                System.out.print("Código: ");
                int codigo = teclado.nextInt();

                Produto p = buscarPorCodigo(codigo);
                if (p == null) {
                    System.out.println("Nenhum produto encontrado com o código: " + codigo);
                    return;
                }

                produtos.remove(p);
            }
        }

        System.out.println("Sistema encerrado.");
    }
}