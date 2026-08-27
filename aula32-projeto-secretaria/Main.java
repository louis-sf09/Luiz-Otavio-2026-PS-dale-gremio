/*
 * Disciplina: 2026-PS
 * Estudante : LUIZ OTAVIO DE SOUZA FREO
 * Data      : 2026.08.27
 * Projeto   : aula32-projeto-secretaria
 * Arquivo   : Main.java
 */

// import: ArrayList = a lista que cresce (o gaveteiro).
// Scanner = a leitura do teclado.
import java.util.ArrayList;
import java.util.Scanner;

/*
 * O BALCAO DA SECRETARIA: nao guarda ficha nenhuma, ele atende.
 * Mostra o menu, le a escolha e chama o metodo que resolve.
 */
public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        // O GAVETEIRO TIPADO: o <Aluno> diz que so entra ficha de aluno aqui.
        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        // while (true) = repete para sempre. A unica saida e o break da opcao 0.
        while (true) {
            System.out.println("================================================");
            System.out.println("   SECRETARIA DO LUIZ OTAVIO");
            System.out.println("================================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matricula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = teclado.nextLine().trim();   // trim: tira espacos das pontas

            // Texto se compara com .equals, nunca com == (isso vale ouro em Java).
            if (opcao.equals("0")) {
                System.out.println("Secretaria fechada. Ate a proxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else if (opcao.equals("3")) {
                buscar(lista, teclado);
            } else if (opcao.equals("4")){
                atualizar(lista, teclado);
            } else if (opcao.equals("5")){
                remover(lista, teclado);
            } else if (opcao.equals("6")){
                relatorio(lista, teclado);
            } else {
                System.out.println("Opcao invalida! Vale 0, 1, 2, 3, 4, 5 ou 6.");
            }
        }
    }

    // Le os dados no blacao, carimba a ficha e guarda no gaveteiro.
    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();
        if (nome.equals("")) {
            System.out.println("Precisa preencher o nome!");
            return;
        }

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();
        if (matricula.equals("")) {
            System.out.println("Precisa preencher a matricula!");
            return;
        }

        // MATRICULA UNICA: busca ANTES de inserir. Se ja existe, desiste.
        // A mesma busca de novo: quarta vez que ela trabalha para voce.
        Aluno existente = buscarPorMatricula(lista, matricula);
        if (existente != null) {
            System.out.println("Ja existe ficha com a matricula " + matricula + "!");
            return;   // sai do metodo agora; nao cadastra
        }
        
        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();
        if (curso.equals("")) {
            System.out.println("Precisa preencher o curso!");
            return;
        }

        System.out.print("Data de nascimento: ");
        String dataNasc = teclado.nextLine().trim();
        if (dataNasc.equals("")) {
            System.out.println("Precisa preencher a data de nascimento!");
            return;
        }

        // new carimba a ficha; add guarda no gaveteiro. Sao duas acoes.
        Aluno novo = new Aluno(nome, matricula, curso, dataNasc);
        lista.add(novo);
        System.out.println("Ficha de " + nome + " arquivada!");
    }

    // Percorre o gaveteiro e imprime ficha por ficha (padrao da Aula 29).
    static void listar(ArrayList<Aluno> lista) {
        if (lista.size() == 0) {
            System.out.println("Nenhuma ficha...");
            return;
        }
        System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + " ---");
        for (int i=0; i<lista.size(); i++) {
            Aluno a = lista.get(i);
            System.out.println(a);   // a impressao chama o toString sozinha
        }
    }

    // O CORACAO DO SISTEMA: devolve a ficha achada, ou null se nao existir.
    // Escrito uma vez, usando quatro vezes ate o fim do projeto.
    static Aluno buscarPorMatricula(ArrayList<Aluno> lista, String matricula) {
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            if (a.getMatricula().equals(matricula)) {
                return a;       // achou: devolve ESTA ficha e para o laco
            }
        }
        return null;            // percorreu tudo e nao achou
    }

    // o balcao pergunta a matriula e usa a busca para responder.
    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula procurada: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);

        // GUARDA: confere o null ANTES de usar o resultado.
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
        } else {
            System.out.println("Achei: " + a);
        }
    }

    // Atualizar reusa a busca: escrever uma vez, chamar quantas vezes precisar.
    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }
        System.out.print("Novo curso de " + a.getNome() + ": ");
        String novoCurso = teclado.nextLine().trim();

        // a variavel a segura a MESMA ficha que esta na lista: mudar por
        // aqui muda o que a listagem mostra depois. Nao precisa reinserir.
        a.setCurso(novoCurso);
        System.out.println("Ficha atualizada: " + a);
    }

    // Acao destrutiva pede confirmacao. Padrao de distema de verdade.
    static void remover(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a remover: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }
        System.out.print("Tem certeza que remove " + a.getNome() + "? (s/n): ");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("s")) {
            lista.remove(a);     // remove ESTA ficha (a mesma referencia achada)
            System.out.println("Ficha removida.");
        } else {
            System.out.println("Remocao cancelada.");
        }
    }

    // RELATORIO: o padrao preparar -> percorrer -> usar, da aula 29
    static void relatorio(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.println("--- RELATORIO DA SECRETARIA ---");
        System.out.println("Total de fichas: " + lista.size());
        System.out.print("Contar alunos de qual curso? ");
        String curso = teclado.nextLine().trim();

        int contador = 0;                          // preparar (ANTES do for)
        for (int i = 0; i < lista.size(); i++) {   // percorrer
            Aluno a = lista.get(i);
            if (a.getCurso().equals(curso)) {
                contador = contador + 1;
            }
        }
        System.out.println("Alunos de " + curso + ": " + contador);  // usar
    }
}