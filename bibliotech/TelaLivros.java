import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableCellRenderer;

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
        setSize(750, 550);
        setLocationRelativeTo(null);

        setDefaultCloseOperation(
            JFrame.DISPOSE_ON_CLOSE
        );

        setLayout(new BorderLayout(8, 8));

        modelo = new DefaultTableModel(
            new Object[]{
                "ID", "Capa", "Título", "Autor", "Ano"
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

        tabela.setRowHeight(85);
            
        tabela.setFont(
            new Font("SansSerif", Font.PLAIN, 14)
        );

        tabela.setBackground(
            new Color(248, 250, 252)
        );

        tabela.setForeground(
            new Color(30, 41, 59)
        );

        tabela.setSelectionBackground(
            new Color(191, 219, 254)
        );

        tabela.getTableHeader().setFont(
            new Font("SansSerif", Font.BOLD, 14)
        );

        tabela.getTableHeader().setBackground(
            new Color(78, 119, 197)
        );

        tabela.getTableHeader().setForeground(
            new Color(255, 255, 255)
        );

        tabela.getColumnModel()
            .getColumn(1)
            .setPreferredWidth(90);

        tabela.getColumnModel()
            .getColumn(1)
            .setCellRenderer(
                new javax.swing.table.DefaultTableCellRenderer() {

                    @Override
                    public java.awt.Component
                            getTableCellRendererComponent(
                                JTable tabela,
                                Object valor,
                                boolean selecionada,
                                boolean foco,
                                int linha,
                                int coluna) {

                        JLabel label = new JLabel();

                        label.setHorizontalAlignment(
                            JLabel.CENTER
                        );

                        label.setOpaque(true);

                        label.setBackground(
                            selecionada
                            ? tabela.getSelectionBackground()
                            : tabela.getBackground()
                        );

                        if (valor instanceof ImageIcon) {
                            label.setIcon((ImageIcon) valor);
                        } else {
                            label.setText("Sem capa");
                        }

                        return label;
                    }
                }
            );

        GridLayout controlesLayout =
            new GridLayout(0, 3, 20, 10);

        JPanel controles = new JPanel(
            new FlowLayout(FlowLayout.LEFT)
        );

        controles.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        JButton buscar =
            new JButton("Buscar por ID");
        buscar.setPreferredSize(new Dimension(200, 30));

        JButton botaoBuscarTitulo =
            new JButton("Buscar por título");

        JButton atualizar =
            new JButton("Atualizar listagem");

        JButton limpar =
            new JButton("Limpar pesquisa");

        JButton botaoCapa =
            new JButton("Selecionar capa");

        controles.setLayout(controlesLayout);

        controles.add(new JLabel("ID do livro:"));
        controles.add(campoId);
        controles.add(buscar);

        controles.add(new JLabel("Título:"));
        controles.add(campoTitulo);
        controles.add(botaoBuscarTitulo);

        controles.add(atualizar);
        controles.add(limpar);
        controles.add(botaoCapa);

        add(controles, BorderLayout.NORTH);
        add(status, BorderLayout.SOUTH);

        buscar.addActionListener(
            e -> buscarLivro()
        );
        campoId.addActionListener(
            e -> buscarLivro()
        );
        botaoBuscarTitulo.addActionListener(
            e -> buscarPorTitulo()
        );
        campoTitulo.addActionListener(
            e -> buscarPorTitulo()
        );
        atualizar.addActionListener(
            e -> carregarLivros()
        );
        limpar.addActionListener(
            e -> {campoTitulo.setText("");
            campoId.setText("");
            carregarLivros();
        });
        botaoCapa.addActionListener(
            e -> selecionarCapa()
        );


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
            carregarMiniatura(livro.getCapa()),
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

    private void selecionarCapa() {

        int linha = tabela.getSelectedRow();

        if (linha == -1) {
            JOptionPane.showMessageDialog(
                this,
                "Selecione um livro na tabela."
            );
            return;
        }

        int linhaModelo =
            tabela.convertRowIndexToModel(linha);

        int id = (int) modelo.getValueAt(
            linhaModelo, 0
        );

        JFileChooser seletor = new JFileChooser();

        seletor.setDialogTitle(
            "Selecione a capa do livro"
        );

        seletor.setFileFilter(
            new javax.swing.filechooser.FileNameExtensionFilter(
                "Imagens JPG e PNG", "jpg", "jpeg", "png"
            )
        );

        if (seletor.showOpenDialog(this)
                != JFileChooser.APPROVE_OPTION) {
            return;
        }

        java.nio.file.Path destino = null;

        try {

            destino = java.nio.file.Path.of(
                ImagemLivro.salvar(
                    seletor.getSelectedFile().toPath(),
                    id
                )
            );

            boolean atualizado =
                dao.atualizarCapa(
                    id, destino.toString().replace('\\', '/')
                );

            if (!atualizado) {

                java.nio.file.Files.deleteIfExists(destino);

                JOptionPane.showMessageDialog(
                    this,
                    "Não foi possível atualizar o livro."
                );

                return;
            }

            carregarLivros();

            JOptionPane.showMessageDialog(
                this,
                "Capa salva com sucesso!"
            );

        } catch (Exception ex) {

            if (destino != null) {
                try {
                    java.nio.file.Files.deleteIfExists(destino);
                } catch (java.io.IOException ignorado) {
                }
            }

            JOptionPane.showMessageDialog(
                this,
                "Erro ao salvar capa: " +
                ex.getMessage()
            );
        }
    }

    private ImageIcon carregarMiniatura(
            String caminho) {

        if (caminho == null || caminho.isBlank()) {
            return null;
        }

        java.io.File arquivo =
            new java.io.File(caminho);

        if (!arquivo.isFile()) {
            return null;
        }

        try {

            java.awt.image.BufferedImage imagem =
                javax.imageio.ImageIO.read(arquivo);

            if (imagem == null) {
                return null;
            }

            Image reduzida = imagem.getScaledInstance(
                55, 75, Image.SCALE_SMOOTH
            );

            return new ImageIcon(reduzida);

        } catch (java.io.IOException e) {
            return null;
        }
    }

    public static void main(String[] args) {

        SwingUtilities.invokeLater(() -> {
            new TelaLivros().setVisible(true);
        });
    }
}