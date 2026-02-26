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
print("Primeiro livro:", titulos[0])
print("Último livro  :", titulos[-1])   # índice -1 = último elemento
print("Total de livros:", len(titulos))

# ---- MÉTODOS DE LISTA ----

print("\n--- Operações na lista ---")

# Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificar se um item existe
busca = "Código Limpo"
if busca in titulos:
    print(f'"{busca}" está no catálogo')
else:
    print(f'"{busca}" não encontrado.')

# Ordenar a lista
titulos.sort()
print("Lista ordenada:", titulos)

# Remover um item
titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)

# Mostra cada titulo e sua posição
for indice, livro in enumerate(titulos):
    print(f"{indice}. {livro}")
