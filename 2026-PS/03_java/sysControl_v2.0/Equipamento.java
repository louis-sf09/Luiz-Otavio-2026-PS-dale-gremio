public class Equipamento {
    /* Atributos privados */
    private String patrimonio;
    private String descricao;
    private int setor;
    private boolean ativo;

    /* Método construtor */
    public Equipamento(String patrimonio, String descricao, int setor, boolean ativo) {
        setPatrimonio(patrimonio);
        setDescricao(descricao);
        setSetor(setor);
        setAtivo(ativo);
    }
}