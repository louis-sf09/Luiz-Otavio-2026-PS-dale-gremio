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
    global emprestados, disponiveis
    emprestados = 0
    disponiveis = 0
    # Percorrendo cada livro com for
    for livro in catalog:
        if livro["disponivel"] == True:
            status = "✅️ Disponivel"
            disponiveis += 1    # contando 1 para os livors disponiveis
        else:
            status = "📚 Emprestado"
            emprestados += 1    # contando 1 para os livros emprestados

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

    if op.lower() == "s":   # testa a resposta do usuário usando .lower()
        # Lê as inormações para adicionar um novo livro ao catálogo
        titulo = input("\n  Titulo do livro: ")
        autor = input("  Autor do livro: ")
        ano = input("  Ano de publicação: ")
        while not ano.isdigit():
            print("\n  Data inválida")
            ano = input("  Ano de publicação: ")

        catalog.append({"titulo": titulo, "autor": autor, "ano": ano, "disponivel": True})
        show_catalog()
    else:
        print("  Ok")
        break

# Buscando livros por autor
while True:
    print("\n --- Busca de livros ---")
    print("\n  Deseja buscar um livro: (s) sim (n) não")
    op = input("  -> ")

    if op.lower() == "s":   # testa a resposta do usuário usando .lower()
        autor = input("  Digite o nome de um autor: ")
        print()

        encontrado = False
        # Percorre a lista em busca de livros do autor digitado
        for livro in catalog:
            if autor.lower() in livro["autor"].lower(): # usa .lower() -> case-insensitive
                status = "✅️ Disponivel" if livro["disponivel"] else "📚 Emprestado"
                print(f'  {livro["titulo"]} ({livro["ano"]})')
                print(f'  Autor: {livro["autor"]} | {status}')
                print(" " + "-" * 55)
                encontrado = True
        if encontrado == False:
            print("\n  Nenhum livro encontrado com o autor informado")
    else:
        print("  Ok")
        break

# Mostrando o relatório final
print("\n --- Relatório ---")
print(f"\n  Livros emprestados 📚: {emprestados}")
print(f"  Livros disponiveis ✅️: {disponiveis}")
