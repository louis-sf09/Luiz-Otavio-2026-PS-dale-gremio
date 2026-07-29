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
        if (ativo) {
            return "ativo";
        } else {
            return "inativo";
        }
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

    /* Métodos de Comportamento */
    public int transferirSetor(int novoSetor) {
        setor = novoSetor;
        return setor;
    }

    public String ativar() {
        if (!ativo) {
            ativo = true;
            return "Sucesso: Equipamento ativado.";
        } else {
            return "Falha: Equipamento já está ativo.";
        }
    }

    public String desativar() {
        if (ativo) {
            ativo = false;
            return "Sucesso: Equipamento ativado.";
        } else {
            return "Falha: Equipamento já está desativado."
        }
    }
}
