import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("=================================");
        System.out.println("      LANCHE OU NET");
        System.out.println("=================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$ 8,00");
        System.out.println("4 - Café ............... R$ 5,00");
        System.out.println("5 - Bolo no Pote ....... R$ 9,00");
        System.out.println("=================================");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();
        int preco = 0;

        if (opcao > 0 && opcao <= 5){
            if (opcao == 1) {
                System.out.println("Você escolheu X-Burguer - R$ 18,00.");
                preco = 18;
            } else if (opcao == 2) {
                System.out.println("Você escolheu Pizza - R$ 35,00.");
                preco = 35;
            } else if (opcao == 3) {
                System.out.println("Você escolheu Suco Natural - R$ 8,00.");
                preco = 8;
            } else if (opcao == 4) {
                System.out.println("Você escolheu Café - R$ 5,00.");
                preco = 5;
            } else if (opcao == 5) {
                System.out.println("Você escolheu Bolo no Pote - R$ 9,00.");
                preco = 9;
            }

            System.out.print("Quantidade desejada: ");
            int qtd = entrada.nextInt();
            System.out.println("Preço total: R$ " + preco*qtd);

        } else {
            System.out.println("Opção inválida.");
        }

        entrada.close();

        System.out.println("Volte sempre! ...");
    }
}
