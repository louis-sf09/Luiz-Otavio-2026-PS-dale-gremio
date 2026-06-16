import java.util.Scanner;
import java.util.Random;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random pedido = new Random();

        int continuar = 1;
        int preco = 0;
        int qtd_x = 0, qtd_p = 0, qtd_s = 0, qtd_c = 0, qtd_b = 0;

        while (continuar == 1)  {
            System.out.println("\n=================================");
            System.out.println("      LANCHE OU NET");
            System.out.println("=================================");
            System.out.println("\n1 - X-Burguer .......... R$ 18,00");
            System.out.println("2 - Pizza .............. R$ 35,00");
            System.out.println("3 - Suco Natural ....... R$ 8,00");
            System.out.println("4 - Café ............... R$ 5,00");
            System.out.println("5 - Bolo no Pote ....... R$ 10,00");
            System.out.println("6 - Finalizar pedido\n");

            System.out.print("\nEscolha: ");
            int opcao = entrada.nextInt();

            if (opcao == 6){

                System.out.println("\n=================================");
                System.out.println("RESUMO DO PEDIDO");
                System.out.println("=================================\n");

                if (qtd_x > 0){
                    System.out.println(qtd_x + "x X-Burguer .......... R$ " + qtd_x*18 + ",00");
                }
                if (qtd_p > 0){
                    System.out.println(qtd_p + "x Pizza .............. R$ " + qtd_p*35 + ",00");
                }
                if (qtd_s > 0){
                    System.out.println(qtd_s + "x Suco Natural ....... R$ " + qtd_s*8 + ",00");
                }
                if (qtd_c > 0){
                    System.out.println(qtd_c + "x Café ............... R$ " + qtd_c*5 + ",00");
                }
                if (qtd_b > 0){
                    System.out.println(qtd_b + "x Bolo no Pote ....... R$ " + qtd_b*10 + ",00");
                } 

                System.out.println("\nTOTAL: R$ " + preco + ",00");

                System.out.println("\nForma de pagamento:");
                System.out.println("1 - Dinheiro");
                System.out.println("2 - Cartão");
                System.out.println("3 - PIX");

                System.out.println("\nEscolha: ");
                opcao = entrada.nextInt();

                if ((opcao>0) && (opcao<4)){
                    System.out.println("\nPagamento realizado com sucesso!");
                    break;
                } else {
                    System.out.println("\nOpção inválida");
                    continue;
                }
            }

            System.out.print("\nQuantidade: ");
            int qtd = entrada.nextInt();

            switch (opcao) {
                case 1:
                    preco += 18 * qtd;
                    qtd_x += qtd;
                    break;
                case 2:
                    preco += 35 * qtd;
                    qtd_p += qtd;
                    break;
                case 3:
                    preco += 8 * qtd;
                    qtd_s += qtd;
                    break;
                case 4:
                    preco += 5 * qtd;
                    qtd_c += qtd;
                    break;
                case 5:
                    preco += 10 * qtd;
                    qtd_b += qtd;
                    break;
                default:
                    System.out.println("Opção inválida");
            }
            System.out.println("\nItem adicionado ao pedido!");
        }

        entrada.close();

        System.out.println("\nPedido n° " + pedido.nextInt(999));

        System.out.println("\nAguarde a chamada do seu pedido.");
    }
}
