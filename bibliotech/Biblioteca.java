import java.util.ArrayList;

public class Biblioteca {

    private ArrayList<Livro> livros;
    private ArrayList<Leitor> leitores;
    private ArrayList<Emprestimo> emprestimos;

    public Biblioteca() {
        this.livros = new ArrayList<Livro>();
        this.leitores = new ArrayList<Leitor>();
        this.emprestimos = new ArrayList<Emprestimo>();
    }

    public void cadastrarLivro(Livro livro) {
        livros.add(livro);
    }

    public boolean cadastrarLeitor(Leitor leitor) {
        for (int i = 0; i < leitores.size(); i++) {
            Leitor l = leitores.get(i);
            if (leitor.getMatricula() == l.getMatricula()) {
                return false;
            }
        }
        leitores.add(leitor);
        return true;
    }

    public void listarAcervo() {
        for (int i = 0; i < livros.size(); i++) {
            System.out.println(livros.get(i));
        }
    }

    public Livro buscarLivro(String titulo) {
        for (int i = 0; i < livros.size(); i++) {
            Livro l = livros.get(i);
            if (l.getTitulo().equals(titulo)) {
                return l;
            }
        }
        return null;
    }

    public Leitor buscarLeitor(String matricula) {
        for (int i =0; i < leitores.size(); i++) {
            Leitor l = leitores.get(i);
            if (l.getMatricula().equals(matricula)) {
                return l;
            }
        }
        return null;
    }

    public boolean emprestar(String titulo, String matricula) {
        Livro livro = buscarLivro(titulo);
        Leitor leitor = buscarLeitor(matricula);
        if(livro == null || leitor == null) {
            return false;
        }
        
        Emprestimo novo = new Emprestimo(livro, leitor);
        if (!novo.realizarEmprestimo()) {
            return false;
        }

        emprestimos.add(novo);
        return true;
    }

    public boolean devolver(String titulo) {
        for (int i = 0; i < emprestimos.size(); i++) {
            Emprestimo e = emprestimos.get(i);
            if (e.estaAtivo() && e.getLivro().getTitulo().equals(titulo)) {
                return e.registrarDevolucao();
            }
        }
        return false;
    }

    public void listarEmprestimos() {
        for (int i = 0; i < emprestimos.size(); i++) {
            System.out.println(emprestimos.get(i));
        }
    }

    public void listarLivrosDoLeitor(String matricula) {
        System.out.println("--- Livros com a matricula " + matricula + " ---");
        for (int i = 0; i < emprestimos.size(); i++) {
            Emprestimo e = emprestimos.get(i);
            if (e.getLeitor().getMatricula() == matricula && e.estaAtivo()) {
                System.out.println(e.getLivro());
            }
        }
    }
}