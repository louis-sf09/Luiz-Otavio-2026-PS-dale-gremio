public class main {
    public static void main(String[] args) {
        produto produto1 = new produto("Mouse", 80.00, 10);

        produto1.adicionarEstoque(5);
        boolean removido = produto1.removerEstoque(3);

        System.out.println("Produto: " + produto1.getNome());
        System.out.println("Preço: R$ " + produto1.getPreco());
        System.out.println("Quantidade: " + produto1.getQuantidade());
        System.out.println("Remoção realizada: " + removido);
        System.out.println("Valor em estoque: R$ " + produto1.calcularValorEmEstoque());
    }
}
