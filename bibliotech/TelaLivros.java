import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.List;

public class TelaLivros extends JFrame {

    private final LivroDAO dao = new LivroDAO();

    private final DefaultTableModel modelo;
    private final JTable tabela;

    private final JTextField campoId =
        new JTextField(8);

    private final JLabel status =
        new JLabel("Pronto.");

    private final JTextField campoTitulo =
        new JTextField(18);

    public TelaLivros() {

        setTitle("BiblioTech - Consulta de Livros");
        setSize(650, 450);
        setLocationRelativeTo(null);

        setDefaultCloseOperation(
            JFrame.DISPOSE_ON_CLOSE
        );

        setLayout(new BorderLayout(8, 8));

        modelo = new DefaultTableModel(
            new Object[]{
                "ID", "Título", "Autor", "Ano"
            }, 0
        ) {
            @Override
            public boolean isCellEditable(
                int linha, int coluna) {
                return false;
            }
        };

        tabela = new JTable(modelo);

        add(
            new JScrollPane(tabela),
            BorderLayout.CENTER
        );

        GridLayout controlesLayout =
            new GridLayout(0, 3, 10, 4);

        JPanel controles = new JPanel(
            new FlowLayout(FlowLayout.LEFT)
        );

        JButton buscar =
            new JButton("Buscar por ID");

        JButton botaoBuscarTitulo =
            new JButton("Buscar por título");

        JButton atualizar =
            new JButton("Atualizar listagem");

        JButton mostrarTodos =
            new JButton("Mostrar todos");

        JButton limpar =
            new JButton("Limpar pesquisa");

        controles.setLayout(controlesLayout);

        controles.add(new JLabel("ID do livro:"));
        controles.add(campoId);
        controles.add(buscar);

        controles.add(new JLabel("Título:"));
        controles.add(campoTitulo);
        controles.add(botaoBuscarTitulo);

        controles.add(atualizar);
        controles.add(mostrarTodos);
        controles.add(limpar);

        add(controles, BorderLayout.NORTH);
        add(status, BorderLayout.SOUTH);

        buscar.addActionListener(e -> buscarLivro());
        campoId.addActionListener(e -> buscarLivro());
        botaoBuscarTitulo.addActionListener(e -> buscarPorTitulo());
        campoTitulo.addActionListener(e -> buscarPorTitulo());
        atualizar.addActionListener(e -> carregarLivros());
        mostrarTodos.addActionListener(e -> carregarLivros());
        limpar.addActionListener(e -> {
            campoTitulo.setText("");
            campoId.setText("");
            carregarLivros();
        });

        carregarLivros();
    }

    private void carregarLivros() {

        modelo.setRowCount(0);

        List<Livro> livros =
            dao.listarLivros();

        for (Livro livro : livros) {
            adicionarLinha(livro);
        }

        status.setText(
            "Livros apresentados: " + livros.size()
        );
    }

    private void adicionarLinha(Livro livro) {

        modelo.addRow(new Object[]{
            livro.getId(),
            livro.getTitulo(),
            livro.getAutor(),
            livro.getAno()
        });
    }

    private void buscarLivro() {

        String texto = campoId.getText().trim();

        int id;

        try {
            id = Integer.parseInt(texto);

            if (id <= 0) {
                throw new NumberFormatException();
            }

        } catch (NumberFormatException ex) {

            JOptionPane.showMessageDialog(
                this,
                "Informe um ID inteiro positivo.",
                "Entrada inválida",
                JOptionPane.WARNING_MESSAGE
            );

            return;
        }

        Livro livro = dao.buscarLivroPorId(id);

        modelo.setRowCount(0);

        if (livro == null) {

            status.setText(
                "Nenhum livro encontrado para o ID " + id
            );

            JOptionPane.showMessageDialog(
                this,
                "Livro não encontrado."
            );

        } else {

            adicionarLinha(livro);

            status.setText(
                "Livro encontrado: " + livro.getTitulo()
            );
        }
    }

    public static void main(String[] args) {

        SwingUtilities.invokeLater(() -> {
            new TelaLivros().setVisible(true);
        });
    }

    private void buscarPorTitulo() {

        String titulo =
            campoTitulo.getText().trim();

        if (titulo.isEmpty()) {

            JOptionPane.showMessageDialog(
                this,
                "Informe o título do livro.",
                "Campo obrigatório",
                JOptionPane.WARNING_MESSAGE
            );

            return;
        }

        List<Livro> livros =
            dao.buscarLivrosPorTitulo(titulo);

        modelo.setRowCount(0);

        for (Livro livro : livros) {
            adicionarLinha(livro);
        }

        status.setText(
            "Livros encontrados: " +
            livros.size()
        );

        if (livros.isEmpty()) {

            JOptionPane.showMessageDialog(
                this,
                "Nenhum livro encontrado."
            );
        }
    }
}