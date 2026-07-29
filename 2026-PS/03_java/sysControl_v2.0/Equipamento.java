/* Equipamento.java */

/* Classe Equipamento */
public class Equipamento {

    /* Atributos privados */
    private String nome;
    private String patrimonio;
    private String descricao;
    private int setor;
    private boolean ativo;

    /* Método construtor */
    public Equipamento(String nome, String patrimonio, String descricao, int setor, boolean ativo) {
        setNome(nome);
        setPatrimonio(patrimonio);
        setDescricao(descricao);
        setSetor(setor);
        setAtivo(ativo);
    }

    /* Getters */
    public String getNome() {
        return nome;
    }

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
            return "Sim";
        } else {
            return "Não";
        }
    }

    /* Setters e Validações */
    public void setNome(String nome) {
        if (nome != null && !nome.isBlank()) {
            this.nome = nome;
        }
    }

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
    public String alterarNome(String novoNome) {
        if (novoNome != null && !novoNome.isBlank()) {
            nome = novoNome;
            return "Sucesso: Alteração realizada - Novo nome: " + nome;  
        }
        return "Falha: novo nome inválido.";
    }

    public String transferirSetor(int novoSetor) {
        if (novoSetor >= 0) {
            setor = novoSetor;
            return "Sucesso: Tranferencia realizada - Novo setor: " + setor;  
        }
        return "Falha: novo número de setor inválido.";
    }

    public String ativar() {
        if (!ativo) {
            ativo = true;
            return "Sucesso: Equipamento ativado.";
        }
        return "Falha: Equipamento já está ativo.";
    }

    public String desativar() {
        if (ativo) {
            ativo = false;
            return "Sucesso: Equipamento ativado.";
        }
        return "Falha: Equipamento já está desativado.";
    }
}
