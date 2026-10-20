public class TesteLivroDAO {

    public static void main(String[] args) {

        /*
        LivroDAO dao = new LivroDAO();

        dao.adicionarLivro("O Senhor dos Anéis", "JRR Tolkien", 1954);
        dao.adicionarLivro("As Crônicas de Nárnia", "CS Lewis", 1950);
        dao.adicionarLivro("1984", "George Orwell", 1949);

        dao.atualizarLivro(1, "Dom Casmurro", "Machado de Assis", 1899);

        dao.excluirLivro(1);
        */

        LivroDAO dao = new LivroDAO();

        boolean atualizou = dao.atualizarLivro(
            999999,
            "Livro Inexistente",
            "Autor Desconhecido",
            2026
        );

        boolean excluiu = dao.excluirLivro(999999);

        System.out.println(
            "Atualização: " + atualizou
        );

        System.out.println(
            "Exclusão: " + excluiu
        );
    }
}