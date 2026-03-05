# ===============================================
# SISTEMA DE CONTROLE DE ESTOQUE
# ===============================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor      : Lui Otávio de S. Freo
# Data       : 2026.02.26
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ===============================================
#
# DESCRIÇÃO:
# Este programa processa os produtos em um estoque, bem como
# suas quantidades, classificando-os de acordo com suas
# quantidades sendo as classificações: Crítico, Adequado, Excesso.
# Conceitos utilizados: variáveis, tipos de dados, operadores,
# estrutuuras de seleção e estruturas de repetição.
# ===============================================

# ------ FUNÇÕES ------
# --- Relatório do Estoque Atual ---
def show_estoque():
    
    exc = 0
    adq = 0
    crt = 0

    # o for percorre todos os produtos da lista
    for produto in estoque:
        nome  = produto["nome"]
        qtd   = produto["qtd"]

        if qtd > 9:
            situacao = "Excesso"
            exc += 1
        elif qtd > 5:
            situacao = "Adequado"
            adq += 1
        else:
            situacao = "Crítico"
            crt += 1

        print(f"Produto    : {nome}")
        print(f"Quantidade : {qtd}")
        print(f"Situação   : {situacao}")
        print("-" * 30) # linha separadora: repete o caractere "-" 30 vezes

    print()
    print("----- Relatório do Estoque -----")
    print()

    # mostra um relatório com a qtd de produtos em cada situação
    print(f"Excesso  : {exc}")
    print(f"Adequado : {adq}")
    print(f"Crítico  : {crt}")
    print("-" * 30)
    
# --- Validação de Entradas ---
def test(op, ops, msg):
    while not op in ops:    # testa se a opção é válida

        print("-" * 30)
        print(msg)
        op = input("-> ")
        op = op.lower()

    return op



# ------ CÓDIGO PRINCIPAL ------
# ---- DADOS DO ESTOQUE ----
estoque = [
    {"nome": "Arroz",     "qtd": 10},
    {"nome": "Farofa",    "qtd":  6},
    {"nome": "Feijão",    "qtd":  3},
    {"nome": "Picanha",   "qtd":  2},
    {"nome": "Cerveja",   "qtd": 15},
    {"nome": "Maionese",  "qtd":  5},
]

print()
print("----- Estoque Atual -----")
print()

show_estoque()

# ---- PESQUISA DE PRODUTOS DO ESTOQUE ----
while True:
    # pergunta se o usuário quer pesquisar por um produto
    print("-" * 30)
    print("\nDeseja pesquisar um produto?\n[s] Sim\n[n] Não")

    msg = "\nDigite uma opção válida!"
    ops = ["s", "n"]
    op  = input("-> ")
    op  = op.lower()
    op  = test(op, ops, msg)    # valida a entrada

    if op == "n":   # caso não queira pesquisar um produto sai do laço
        break

    # pede o nome do produto
    print("-" * 30)
    print("\nDigite o nome do produto: ")
    op  = input("-> ")

    erro = True
    for produto in estoque:             # verifica se o produto existe no estoque
        if op == produto["nome"]:
            nome  = produto["nome"]
            qtd   = produto["qtd"]

            if qtd > 9:
                situacao = "Excesso"
            elif qtd > 5:
                situacao = "Adequado"
            else:
                situacao = "Crítico"

            # mostra o produto buscado caso seja encontrado
            print("-" * 30)
            print(f"Produto    : {nome}")
            print(f"Quantidade : {qtd}")
            print(f"Situação   : {situacao}")
            print("-" * 30)

            erro = False
            break

    if erro == True:    # caso o produto não esteja em estoque
        print("\nEsse produto não está cadastrado.")

# ---- ADIÇÃO DE PRODUTOS DO ESTOQUE ----
while True:
    # pegunta ao usuário se ele deseja adicionar um novo produto a lista
    print("-" * 30)
    print("\nDeseja adicionar um produto?\n[s] Sim\n[n] Não")

    msg = "\nDigite uma opção válida!"
    ops = ["s", "n"]
    op  = input("-> ")
    op  = op.lower()
    op  = test(op, ops, msg)

    if op == "n":
        break

    # pede o nome e a qtd em estoque do novo produto
    print("-" * 30)
    print("\nDigite o nome do produto:")
    op  = input("-> ")
    nome_p = op

    print("-" * 30)
    print("\nDigite a qtd em estoque do produto:")
    op  = input("-> ")

    while not op.isdigit():                         # testa se a qtd informada é válida
        print("\nDigite uma quantidade válida:")
        op  = input("-> ")
        if op.isdigit:
            if int(op) < 0:
                op = "a"
    
    qtd_p = op

    estoque.append({"nome": nome_p, "qtd": int(qtd_p)},)    # adiciona o produto a lista

# ---- ENCERRAMENTO DO PROGRAMA ----
critico = estoque[0]["qtd"]
for produto in estoque:             # verifica qual o produto mais critico
    if int(produto["qtd"]) < critico:
        nome    = produto["nome"]
        qtd     = produto["qtd"]
        critico = qtd

print()
print("-" * 30)
show_estoque()  # mostra o estoque novamente, com os novos produtos caso tenham sido adicionados

# mostra o produto mais escasso e finaliza o programa
print()
print("-" * 30)
print(f"Produto mais escasso : {nome}")
print(f"Quantidade em estoque: {critico}")
print("-" * 30)
print()

print("\nTchau!\nVolte em breve!")
