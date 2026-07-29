/* Main.java */

/* Classe Main */
public class Main {
    public static void main(String[] args) {

        /* Objeto 1 */
        Equipamento equipamento1 = new Equipamento("Equipamento 1", "Luiz O.", "de S. F.", 25, true);
        System.out.println("\n--- " + equipamento1.getNome() + " ---");
        System.out.println("Patrimônio: " + equipamento1.getPatrimonio());
        System.out.println("Descrição:  " + equipamento1.getDescricao());
        System.out.println("Setor:      " + equipamento1.getSetor());
        System.out.println("Ativo:      " + equipamento1.getAtivo());

        /* Objeto 2 */
        Equipamento equipamento2 = new Equipamento("Equipamento 2", "Público", "Ruim e barato", 9, false);
        System.out.println("\n--- " + equipamento2.getNome() + " ---");
        System.out.println("Patrimônio: " + equipamento2.getPatrimonio());
        System.out.println("Descrição:  " + equipamento2.getDescricao());
        System.out.println("Setor:      " + equipamento2.getSetor());
        System.out.println("Ativo:      " + equipamento2.getAtivo());

        /* Objeto 3 */
        Equipamento equipamento3 = new Equipamento("Equipamento", "Privado", "Bom e caro", 2009, true);
        System.out.println("\n--- " + equipamento3.getNome() + " ---");
        System.out.println("Patrimônio: " + equipamento3.getPatrimonio());
        System.out.println("Descrição:  " + equipamento3.getDescricao());
        System.out.println("Setor:      " + equipamento3.getSetor());
        System.out.println("Ativo:      " + equipamento3.getAtivo());

        /* Tentativas de alteração */
        System.out.println("\n--- Tentativas de alteração ---");
        System.out.println("Alterar nome eq. 3:      " + equipamento3.alterarNome(""));
        System.out.println("Transferir setor eq. 1:  " + equipamento1.transferirSetor(-2));
        System.out.println("Desativar eq. 2:         " + equipamento2.desativar());
        System.out.println("Ativar eq. 2:            " + equipamento2.ativar());

    }
}
