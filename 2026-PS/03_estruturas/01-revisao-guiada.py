# ===================================================
# SISTEMA DE BIBLIOTECA
# ===================================================
# Disciplina : Progrmação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Luiz Otávio de S. Freo
# Data       : 2026.26.02
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ===================================================
#
# DESCRIÇÃO:
# Catálogo de livors que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.
# ===================================================

# ---- LISTAS: CONCEITO BÁSICO ----

# Criando uma lista de títulos
titulos = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritmos",
]

# Acesso por índice (começa em 0, não em 1!)
print("\nPrimeiro livro:", titulos[0])
print("Último livro  :", titulos[-1])   # índice -1 = último elemento
print("Total de livros:", len(titulos))



# ---- MÉTODOS DE LISTA ----

print("\n--- Operações na lista ---\n")

# Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificar se um item existe
busca = "Código Limpo"
if busca in titulos:
    print(f'\n"{busca}" está no catálogo')
else:
    print(f'\n"{busca}" não encontrado.')

# Ordenar a lista
titulos.sort()
print("\nLista ordenada:", titulos)

# Remover um item
titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)
print()

# Mostra cada titulo e sua posição
for indice, livro in enumerate(titulos):
    print(f"{indice}. {livro}")
print("\n\n\n")



# ---- DICIONÁRIOS: CONCEITO BÁSICO ----

# Um dicionário representa um livro com seus atributos
livro = {
    "titulo":       "O Programador Pragmático",
    "autor":        "Andrew Hunt",
    "ano":          1999,                   # int, não string
    "disponivel":   True,                   # bool         
}

# Acessando valores pelas chaves
print("Titulo :", livro["titulo"])
print("Autor  :", livro["autor"])
print("Ano    :", livro["ano"])
print("Status :", "Disponivel" if livro["disponivel"] else "Emprestado")



# ---- MODIFICANDO E CONSULTANDO ----

# Atualizando um valor existente
livro["disponivel"] = False     # livro foi emprestado
print("\nApós empréstimo:", livro["disponivel"])

# Adicionando uma nova chave
livro["paginas"] = 352
print("Páginas:", livro["paginas"])

# .get() - acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora", "Não informada")
print("Editora:", editora)    # não lança KeyError, retorna o padrão
print("\n\n\n")



# ---- CATÁLOGO: LISTA DE DICIONÁRIOS ----

catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999, "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponivel": False},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016, "disponivel": True},
]

print("=== Catálogo da Biblioteca ===")
print()

# Percorrendo cada livro com for
for livro in catalogo:
    status = "✅️ Disponivel" if livro["disponivel"] else "📚 Emprestado"
    print(f'  {livro["titulo"]} ({livro["ano"]})')
    print(f'  Autor: {livro["autor"]} | {status}')
    print(" " + "-" * 40)



# ---- CONSULTAS E FILTROS ----

print("\n=== Livros disponiveis ===")
for livro in catalogo:
    if livro["disponivel"]:                 # filtra apenas os disponiveis
        print(f'  ✅️ {livro["titulo"]}')

print("\n=== Busca por titulo ===")
busca = input("Digite o titulo (ou parte): ").lower()
encontrado = False
for livro in catalogo:
    if busca in livro["titulo"].lower():    # .lower() ignora maiúsculas/minúsculas
        print(f'  Encontrado: {livro["titulo"]} - {livro["autor"]}')
        encontrado = True
if not encontrado:
    print("  Nenhum livro encontrado com esse termo.")

print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items():    # .items() retorna pares (chave, valor)
    print(f"  {chave}: {valor}")
