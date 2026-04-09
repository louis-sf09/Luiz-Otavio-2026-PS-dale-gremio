# ===============================================
# SISTEMA IFesta
# ===============================================
# Disciplina : Programação de Sistemas (PS)
# Aulas      : 12 e 13 - Mini projeto Integrador
# Autores    : Anna Clara Comin, Luiz Otávio de Souza Freo
# Data       : 2026.04.09
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ===============================================
#
# DESCRIÇÃO:
# Este é um sistema de lista de convidados de festas, que
# utiliza funções para cadastrar convidados, buscar
# convidados e alterar a presença deles, utilizando try/except
# para impedir que o código quebre, e persistência
# de dados em arquivos .txt.
# ===============================================

from datetime import datetime

ARQUIVO   = "dados.txt"
SEPARADOR = "|"

def carregar_lista():
    """Lê o .txt e reconstrói a lista de dicionários."""
    lista_convidados = []
    try:                # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar

        with open(ARQUIVO, "r", encoding="utf-8") as f:     # abrindo com "r" apenas leitura do arquivo
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:
                    continue
                nome, idade, presenca_str = partes
                lista_convidados.append({
                    "nome":      nome,
                    "idade":     idade,
                    "presenca":  presenca_str == "True"
                })

    except FileNotFoundError:
        pass                    # se o arquivo ainda não tiver sido criado não quebra o código
    return lista_convidados



def listar_convidados(lista_convidados):
    """Exibe a lista de convidados."""
    print("\n" + "=" * 50)
    print("  🎉 LISTA DE CONVIDADOS")
    print("=" * 50)

    if not lista_convidados:
        print("  Nenhum convidado encontrado.")
        return
    
    for i, pessoa in enumerate(lista_convidados):
        status = "✅ Presente" if pessoa["presenca"] else "❌ Ausente"
        print(f"{i+1}. {pessoa['nome']} - {pessoa['idade']} ano(s) [{status}]")

    print("=" * 50)



def buscar_convidado(lista_convidados):
    """Possibilita buscar um convidado da lista  por nome ou idade."""
    if not lista_convidados:
        print("  Nenhum convidado encontrado.")
        return
    
    print("\n--- Buscar Convidado ---")
    opcoes = {
        "1": ("Buscar por nome", "Digite parte do nome cadastrado: ", "nome"),
        "2": ("Buscar por idade", "Digite a idade desejada: ", "idade"),
    }

    print("\n  Opções:")
    for chave, (descricao, _, _) in opcoes.items():
        print(f"  [{chave}] {descricao}")
    escolha = input("\n  Sua escolha: ")

    if escolha not in opcoes:           # se a opção não for válida retorna ao menu
        print("❌ Opção inválida")
        return

    _, msg, criterio = opcoes[escolha]
    termo = input(msg).strip().lower()

    try:
        resultados = [p for p in lista_convidados if termo in str(p[criterio]).lower()]    # procura por nomes na lista que tenham o termo digitado

        if not resultados:
            print("  Nenhum convidado encontrado.")
            return
        
        print(f"\n  ({len(resultados)} resultado(s):")
        for pessoa in resultados:
            status = "✅ Presente" if pessoa["presenca"] else "❌ Ausente"
            print(f"  • {pessoa['nome']} - {pessoa['idade']} [{status}]")

    except Exception as e:                  # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        print(f"❌ Erro inesperado: {e}")



def salvar_lista(lista_convidados):
    """Grava a lista de convidados no arquivo .txt."""
    try:
       with open(ARQUIVO, "w", encoding="utf-8") as f:      # abrindo o arquivo com "w" reescreve o arquivo inteiro
            for pessoa in lista_convidados:
                linha = f"{pessoa['nome']}{SEPARADOR}{pessoa['idade']}{SEPARADOR}{pessoa['presenca']}\n"
                f.write(linha)

    except IOError as e:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # IOError: disco cheio, permissão negada, etc.
        print(f"❌ Erro ao salvar: {e}")
        return
    
    print(f"💾 Informações salvas em '{ARQUIVO}'.")



def adicionar_convidado(lista_convidados):
    """Adiciona um novo convidado a lista."""
    print("\n--- Adicionar Novo Convidado ---")

    try:
        # Tipos de dados (Bool, String, Int)
        presenca = False
        nome     = str(input("Digite seu nome: "))
        idade    = int(input("Digite sua idade: "))
        
    except ValueError:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # ValueError: valor não corresponde com o tipo da variável -> exemplo: int(abc)
        print("❌ Idade precisa ser um número!")

    else:                               # executa apenas se o try/except não tiver erros
        if not nome or not idade:
            print("⚠️ Nome é obrigatório.")
            return

        duplicadas = [p for p in lista_convidados if nome.lower() == p["nome"].lower() and str(idade) == str(p["idade"])]         # se o nome e idade deste convidado já existirem conta esse convidado como duplicado

        if len(duplicadas) > 0:
            print("⚠️ Convidado já cadastrado.")
            return

        lista_convidados.append({
            "nome":       nome,
            "idade":      idade,
            "presenca":   presenca
        })
        print(f"✅  Convidado cadastrado com sucesso!")
        salvar_lista(lista_convidados)


def remover_convidado(lista_convidados):
    """Remove um convidado da lista."""
    listar_convidados(lista_convidados)
    if not lista_convidados:
        return
    print("\n--- Remover Convidado ---")

    try:
        numero = int(input("Digite o número do convidado: "))
        if numero <= 0:
            print("❌ Número fora da lista. Verifique os convidados cadastrados.")
            return
        lista_convidados.pop(numero-1)

        print("✅  Convidado removido.")
        salvar_lista(lista_convidados)

    except ValueError:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # ValueError: valor não corresponde com o tipo da variável -> exemplo: int(abc)
        print("❌ Digite apenas o número do convidado.")
    except IndexError:
        # IndexError: intervalo fora da lista -> Exemplo: lista = [a, b, c]   lista[6]
        print("❌ Número fora da lista. Verifique os convidados cadastrados.")
    


def alterar_presenca(lista_convidados):
    """Altera a presença de um dos convidados. Se Presente vira Ausente e vice-versa."""
    listar_convidados(lista_convidados)
    if not lista_convidados:
        return
    print("\n--- Alterar a Frequência ---")

    try:
        numero = int(input("Digite o número do convidado: "))
        pessoa = lista_convidados[numero - 1]

        if pessoa["presenca"]:
            pessoa["presenca"] = False
        else:
            pessoa["presenca"] = True

        print("✅ Presença alterada.")
        salvar_lista(lista_convidados)

    except ValueError:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # ValueError: valor não corresponde com o tipo da variável -> exemplo: int(abc)
        print("❌ Digite apenas o número do convidado.")
    except IndexError:
        # IndexError: intervalo fora da lista -> Exemplo: lista = [a, b, c]   lista[6]
        print("❌ Número fora da lista. Verifique os convidados cadastrados.")



def relatorio(lista_convidados):
    """Exibe um breve relatório da lista de convidados (total de convidados, presentes e ausentes)"""
    total     = 0
    presentes = 0
    ausentes  = 0

    for pessoa in lista_convidados:
        total = total + 1               # operador artimnético +
        # Estrutura de condição if/else
        if pessoa["presenca"]:
            presentes = presentes + 1   # operador artimnético +
        else:
            ausentes =  ausentes + 1    # operador artimnético +
    
    print("\n--- Relatório ---")
    print(f"  Total de convidados: {total}")
    print(f"  Convidados presente: {presentes}")
    print(f"  Convidados ausentes: {ausentes}")



def menu():
    """Função principal do projeto que apresenta as opções dele."""
    lista_convidados = carregar_lista()
    print("\n --- IFesta --- \n")
    print("  Seja bem-vindo ao nosso sistema!\n")
    print("  Selecione uma opção:")

    opcoes = {
        "1": ("Listar convidados",       listar_convidados),
        "2": ("Buscar convidados",       buscar_convidado),
        "3": ("Adicionar convidado",     adicionar_convidado),
        "4": ("Remover convidado",       remover_convidado),
        "5": ("Alterar presença",        alterar_presenca),
        "6": ("Relatório",               relatorio),
        "0": ("Sair",                    None),
    }

    while True:                 # executa até o laço ser quebrado por Erro ou pela função "sair"
        print("\n  Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")

        try:
            escolha = input("\n  Sua escolha: ").strip()
            if escolha not in opcoes:       # operador lógico not
                raise ValueError(f"Opção '{escolha}' inválida.")
            
        except ValueError as e:
            print(f"⚠️  {e}")
            continue

        else:
            # Estrutura de condição
            if escolha == "0":      # operador relacional ==
                print("\n  Até logo: 🎊")
                break
            _, funcao = opcoes[escolha]
            funcao(lista_convidados)



if __name__ == "__main__":  # executa apenas quando esse arquivo é chamado diretamente -> python projeto.py
    menu()
