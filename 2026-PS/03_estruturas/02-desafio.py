# ===================================================
# SISTEMA DE BIBLIOTECA
# ===================================================
# Disciplina : Progrmação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Luiz Otávio de S. Freo
# Data       : 2026.04.03
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ===================================================
#
# DESCRIÇÃO:
# Catálogo de livors que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.
# ===================================================

# ---- FUNÇÕES ----
# Mostra o catálogo
def show_catalog():
    print(" --- Catálogo Atual ---")
    # Percorrendo cada livro com for
    for livro in catalog:
        status = "✅️ Disponivel" if livro["disponivel"] else "📚 Emprestado"
        print(f'  {livro["titulo"]} ({livro["ano"]})')
        print(f'  Autor: {livro["autor"]} | {status}')
        print(" " + "-" * 55)



# ---- CÓDIGO PRINCIPAL ----
# Declarando a lista com os livors
catalog = [
    {"titulo": "O Hobbit", "autor": "J.R.R Tolkien", "ano": 1937,"disponivel": True},
    {"titulo": "As crônicas de nárnia: O cavalo e seu menino", "autor": "C.S. Lewis", "ano": 1954,"disponivel": True},
    {"titulo": "Memórias póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881,"disponivel": True},
]

show_catalog()

# Cadastrando livros
while True:
    print("\n --- Cadastro de livros ---")
    print("\n  Deseja cadastrar um livro: (s) sim (n) não")
    op = input("  -> ")

    if op.lower() == "s":   # verifica se o usuário deseja cadatras um livro
        # Lê as inormações para adicionar um novo livro ao catálogo
        titulo = input("Titulo do livro: ")
        autor = input("Autor do livro: ")
        ano = input("Ano de publicação: ")
        while not ano.isdigit():
            print("\nData inválida")
            ano = input("Ano de publicação: ")

        catalog.append({"titulo": titulo, "autor": autor, "ano": ano, "disponivel": True})
        show_catalog()
    else:
        print("  Ok")
        break
