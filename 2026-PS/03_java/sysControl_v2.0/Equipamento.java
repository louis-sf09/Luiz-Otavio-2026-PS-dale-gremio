/* Equipamento.java */

/* Classe Equipamento */
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

    /* Getters */
    public String getPatrimonio() {
        return patrimonio;
    }

    public String getDescricao() {
        return descricao;
    }

    public int getSetor() {
        return setor;
    }

    public String getAtivo() {
        return "Ativo" if ativo else "Inativo";
    }

    /* Setters e Validações */
    public void setPatrimonio(String patrimonio) {
        if (patrimonio != null && !patrimonio.isBlank()) {
            this.patrimonio = patrimonio;
        }
    }

    public void setDescricao(String descricao) {
        if (descricao != null && !descricao.isBlank()) {
            this.descricao = descricao;
        }
    }

    public void setSetor(int setor) {
        if (setor >= 0) {
            this.setor = setor;
        }
    }

    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }
}
