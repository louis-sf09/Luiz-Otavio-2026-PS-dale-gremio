# ===============================================
# SISTEMA DE CADASTRO DE CLUBE
# ===============================================
# Disciplina : Programação de Sistemas (PS)
# Aulas      : 12 e 13 - Mini projeto Integrador
# Autores    : Anna Clara Comin, Luiz Otávio de Souza Freo
# Data       : 2026.03.26
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ===============================================
#
# DESCRIÇÃO:
# Este é um sistema de cadastro de um clube, que
# utiliza funções para realizar cadastros, buscar
# cadastros e alterar frequencias, utilizando try/except
# para impedir que o código quebre, e persistência
# de dados em arquivos .txt.
# ===============================================

from datetime import datetime

ARQUIVO   = "dados.txt"
HISTORICO = "historico.txt"
SEPARADOR = "|"

def carregar_cadastro():
    """Lê o .txt e reconstrói a lista de dicionários."""
    cadastro = []
    try:                # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar

        with open(ARQUIVO, "r", encoding="utf-8") as f:     # abrindo com "r" apenas leitura do arquivo
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 4:
                    continue
                codigo, nome, idade, ativo_str = partes
                cadastro.append({
                    "codigo": codigo,
                    "nome":   nome,
                    "idade":  idade,
                    "ativo":  ativo_str == "True"
                })

    except FileNotFoundError:
        pass                    # se o arquivo ainda não tiver sido criado não quebra o código
    return cadastro



def listar_cadastros(cadastro):
    """Exibe os cadastros do clube."""
    print("\n" + "=" * 50)
    print("  🏐 CADASTROS DO CLUBE")
    print("=" * 50)

    if not cadastro:
        print("  Nenhum cadastrado encontrado.")
        return
    
    for pessoa in cadastro:
        status = "✅ Ativo" if pessoa["ativo"] else "❌ Inativo"
        print(f"  {pessoa['codigo']}. {pessoa['nome']} - {pessoa['idade']} ano(s) [{status}]")

    print("=" * 50)



def buscar_cadastro(cadastro):
    print("\n--- Buscar Cadastro ---")
    opcoes = {
        "1": ("Buscar por nome", "Digite parte do nome cadastrado: ", "nome"),
        "2": ("Buscar por idade", "Digite a idade desejada: ", "idade"),
        "3": ("Buscar por código", "Digite o código do cadastro: ", "codigo")
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
        resultados = [p for p in cadastro if termo in str(p[criterio]).lower()]    # procura por nomes no cadastro que tenham o termo digitado

        if not resultados:
            print("  Nenhum cadastro encontrado.")
            return
        
        print(f"\n  ({len(resultados)} resultado(s):")
        for pessoa in resultados:
            status = "Ativo" if pessoa["ativo"] else "Inativo"
            print(f"  • {pessoa['nome']} - {pessoa['idade']} [{status}]")

    except Exception as e:                  # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        print(f"❌ Erro inesperado: {e}")



def salvar_cadastro(cadastro):
    """Grava a lista dos cadastros no arquivo .txt."""
    try:
       with open(ARQUIVO, "w", encoding="utf-8") as f:      # abrindo o arquivo com "w" reescreve o arquivo inteiro
            for pessoa in cadastro:
                linha = f"{pessoa['codigo']}{SEPARADOR}{pessoa['nome']}{SEPARADOR}{pessoa['idade']}{SEPARADOR}{pessoa['ativo']}\n"
                f.write(linha)

    except IOError as e:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # IOError: disco cheio, permissão negada, etc.
        print(f"❌ Erro ao salvar: {e}")
        return
    
    print(f"💾 Cadastro salvo em '{ARQUIVO}'.")



def fazer_cadastro(cadastro):
    """Adiciona um novo cadastro ao sistema."""
    print("\n--- Adicionar Novo Cadastro ---")

    if len(cadastro) == 0:
        codigo = "1"
    else:
        codigo = int(cadastro[-1]["codigo"]) + 1
        codigo = str(codigo)

    try:
        nome   = input("Digite seu nome: ")
        idade  = int(input("Digite sua idade: "))
        
    except ValueError:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # ValueError: valor não corresponde com o tipo da variável -> exemplo: int(abc)
        print("❌ Idade precisa ser um número!")

    else:                               # executa apenas se o try/except não tiver erros
        if not nome or not idade:
            print("⚠️ Nome é obrigatório.")
            return

        duplicadas = [p for p in cadastro if nome.lower() == p["nome"].lower() and str(idade) == str(p["idade"])]         # se o nome e idade deste cadastro já existirem conta esse cadastro como duplicado

        if len(duplicadas) > 0:
            print("⚠️ Cadastro já existente.")
            return

        cadastro.append({
            "codigo":     codigo,
            "nome":       nome,
            "idade":      idade,
            "ativo": True
        })
        print(f"✅  Cadastro realizado com sucesso!")
        registrar_historico(nome, "Cadastro adicionado")
        salvar_cadastro(cadastro)



def alterar_frequencia(cadastro):
    """Altera a frequencia de um dos cadastros. Se Ativo vira Inativo e vice-versa."""
    listar_cadastros(cadastro)
    if not cadastro:
        return
    print("\n--- Alterar a Frequência ---")

    try:
        numero = int(input("Digite o número do cadastro: "))
        pessoa = cadastro[numero - 1]

        if pessoa["ativo"]:
            pessoa["ativo"] = False
            registrar_historico(pessoa["nome"], "Alteração frequência [Ativo -> Inativo]")
        else:
            pessoa["ativo"] = True
            registrar_historico(pessoa["nome"], "Alteração frequência [Inativo -> Ativo]")

        print("✅ Frequencia alterada.")
        salvar_cadastro(cadastro)

    except ValueError:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # ValueError: valor não corresponde com o tipo da variável -> exemplo: int(abc)
        print("❌ Digite apenas o número do cadastro.")
    except IndexError:
        # IndexError: intervalo fora da lista -> Exemplo: lista = [a, b, c]   lista[6]
        print("❌ Número fora da lista. Verifique os cadastros.")



def ver_historico(cadastro):
    """Lê o .txt e exibe o histórico de cadastros e alterações de frequência."""
    print("\n--- Histórico de Cadastros e Alterações de Frequência ---")
    try:
        with open(HISTORICO, "r", encoding="utf-8") as f:       # abre o arquivo usando "r" só para leitura
            for linha in f:
                linha = linha.strip()
                if not linha:           # ignora linhas vazias
                    continue
                partes = linha.split(SEPARADOR)
                nome, acao, data = partes
                print(f"  Nome: {nome} - {acao} em: {data}")
                
    except FileNotFoundError:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        pass    #  se o arquivo ainda não tiver sido criado não quebra o código
    return



def registrar_historico(nome, acao):
    """Registra todo cadastro/alteração de frequência no arquivo historico.txt."""
    try:
        # 'a' = append: adiciona informações ao arquivo
        with open(HISTORICO, "a", encoding="utf-8") as f:       # abre o arquivo usando "a" para adicionar informações sem reescrever o arquivo
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            f.write(f"{nome}|{acao}|{data}\n")
    except IOError as e:                 # try/except -> se tiver erro mostra uma msg e continua a execução sem quebrar
        # IOError: disco cheio, permissão negada, etc.
        print(f"❌ Erro ao registrar: {e}")



def relatorio(cadastro):
    """Exibe um breve relatório do clube (qtd de cadastros, ativos e inativos)"""
    total    = 0
    ativos   = 0
    inativos = 0

    for pessoa in cadastro:
        total += 1
        if pessoa["ativo"]:
            ativos += 1
        else:
            inativos += 1
    
    print("\n--- Relatório do Clube ---")
    print(f"  Total de cadastros: {total}")
    print(f"  Pessoas ativas:     {ativos}")
    print(f"  Pessoas inativas:   {inativos}")



def menu():
    """Função principal do projeto que apresenta as opções dele."""
    cadastro = carregar_cadastro()
    print("\n --- Sistema de Cadastro de Clube --- \n")
    print("  Seja bem-vindo ao nosso clube!\n")
    print("  Selecione uma opção:")

    opcoes = {
        "1": ("Listar cadastros",       listar_cadastros),
        "2": ("Buscar cadastro",        buscar_cadastro),
        "3": ("Fazer cadastro",         fazer_cadastro),
        "4": ("Alterar frequencia",     alterar_frequencia),
        "5": ("Ver histórico",          ver_historico),
        "6": ("Relatório",              relatorio),
        "0": ("Sair",                   None),
    }

    while True:                 # executa até o laço ser quebrado por Erro ou pela função "sair"
        print("\n  Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")

        try:
            escolha = input("\n  Sua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")
            
        except ValueError as e:
            print(f"⚠️  {e}")
            continue

        else:
            if escolha == "0":
                print("\n  Até logo: 🏐")
                break
            _, funcao = opcoes[escolha]
            funcao(cadastro)



if __name__ == "__main__":  # executa apenas quando esse arquivo é chamado diretamente -> python projeto.py
    menu()
