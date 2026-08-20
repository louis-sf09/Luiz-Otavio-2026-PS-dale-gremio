/*
 * Disciplina: 2026-PS
 * Estudante : LUIZ OTAVIO DE SOUZA FREO
 * Data      : 2026.08.19
 * Projeto   : aula32-projeto-secretaria
 * Arquivo   : Aluno.java
 */

/*
 * A CLASSE E O MOLDE DA FICHA
 * Ela nao guarda os dados de ninguem: descreve o que TODA ficha de aluno
 * tem (nome, matricula, curso) e o que ela sabe fazer. Cada "new Aluno(...)"
 * no Main carimba uma ficha nova a partir dete molde.
 * Regra de Java: o arquivo tem o mesmo nome da classe publica - Aluno.java
 */
public class Aluno {

    // ATRIBUTOS: os campos impressos na ficha.
    // "private" = so o codigo DESTA classe mexe neles. De fora ninguem
    // escreve direto; tem que passar pelos metodos publicos la embaixo.
    private String nome;
    private String matricula;
    private String curso;

    // CONSTRUTOR: roda no momento do "new" e preenche a ficha.
    // E o __init__ de voces, em Java. Tem o mesmo nome da classe e nao
    // declara tipo de retorno. Os valores chegam de fora, entre parenteses.
    public Aluno(String nome, String matricula, String curso) {
        // "this" = ESTA ficha aqui (a self do Java).
        // this.nome e o atributo da ficha; nome, sozinho, e o parametro
        // que acabou de chegar. Sem o this, os dois seriam o parametro.
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }

    // GETTERS: as janelas de leitura da ficha.
    // Devolvem o valor guardado sem deixar ninguem de fora alterar.
    // Padrao do nome: get + Atributo, com a primeira letra maiuscula.
    public String getNome() {
        return nome;
    }

    public String getMatricula() {
        return matricula;
    }

    public String getCurso() {
        return curso;
    }

    // SETTERS: a unica porta de entrada para mudar um dado da ficha.
    // Hoje eles so trocam o valor, mas e aqui que um dia entra a regra
    // ("nome vazio nao vale", "curso tem que existir").
    // Repare que nao existe setMatricula: matricula nao muda, por decisao
    // do projeto. Sem setter ninguem altera - nem por engano.
    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }
}