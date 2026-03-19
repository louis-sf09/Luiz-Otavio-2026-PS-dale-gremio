# ===============================================
# SISTEMA DE BIBLIOTECA
# ===============================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 10 - Try/Except e Persistência em arquivos .txt
# Autor      : Luiz Otávio de Souza Freo
# Data       : 2026.03.19
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ===============================================
#
# DESCRIÇÃO:
# Este é um sistema de biblioteca com diferentes funções de
# gerenciamento de livros, que utiliza Try/Excepty para impedir
# quebras do programa, e armazena as informações de longo prazo
# em arquivos .txt que podem ser acessados posteriormente.
# ===============================================

from datetime    import datetime
from collections import Counter

# Centralizar o nome evita erros de digitação em todo o código
ARQUIVO   = "biblioteca.txt"
HISTORICO = "historico.txt"
SEPARADOR = "|"   # separa campos em cada linha do .txt

# Formato de cada linha no arquivo
#   titulo|autor|disponivel
# Exemplo
#   Código Limpo|Robert C. Martin|False

def carregar_catalogo():
    """Lê o .txt e reconstrói a lista de dicionários"""
    catalogo = []
    try:
        # o 'r' = leitura | enconding='utf-8' garante acentos corretos
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:           # ignora linhas vazias
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:    # linha malformada -> pula
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo":     titulo,
                    "autor":      autor,
                    # a string "True" no arquivo precisa virar bool True
                    "disponivel": disponivel_str == "True"
                })
    except FileNotFoundError:
        pass    # primeira execução: arquivo ainda não existe - tudo bem
    return catalogo



def salvar_catalogo(catalogo):
    """Grava toda a lista no arquivo .txt."""
    try:
        # 'w' = write: cria se não existir, subscreve se existir
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in catalogo:
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)
        print(f"💾 Catálogo salvo em '{ARQUIVO}'.")
    except IOError as e:
        # IOError: disco cheio, permissão negada, etc.
        print(f"❌ Erro ao salvar: {e}")



def listar_livros(catalogo):
    """Exibe todos os livros com numeração e status."""
    print("\n" + "=" * 50)
    print("  📚 CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not catalogo:
        print("  Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponivel" if livro["disponivel"] else "❌ Emprestado"
        print(f"  {i}. {livro['titulo']} - {livro['autor']} [{status}]")

    print("=" * 50)



def adicionar_livro(catalogo):
    """Coloca dados via input e adiciona um novo livro ao catálogo"""
    print("\n--- Adicionar Novo Livro ---")

    titulo = input("Titulo: ").strip()
    autor  = input("Autor : ").strip()

    if not titulo or not autor:
        print("⚠️ Titulo e autor são obrigatórios.")
        return
    
    duplicadas = [l for l in catalogo if titulo.lower() in l["titulo"].lower()]

    if len(duplicadas) > 0:
        print("⚠️ Titulo já existente no catalogo.")
        return

    catalogo.append({
        "titulo":     titulo,
        "autor":      autor,
        "disponivel": True
    })
    print(f"✅  '{titulo}' adicionado com sucesso!")
    salvar_catalogo(catalogo)



def buscar_livro(catalogo):
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do titulo: ").strip().lower()

    try:
        resultados = [l for l in catalogo if termo in l["titulo"].lower()]

        if not resultados:
            print("  Nenhum livro encontrado.")
            return
        
        print(f"\n  ({len(resultados)} resultado(s):")
        for livro in resultados:
            status = "Disponivel" if livro["disponivel"] else "Emprestado"
            print(f"  • {livro['titulo']} - {livro['autor']} [{status}]")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")



def registrar_emprestimo(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return
    print("\n--- Registrar Empréstimo ---")

    try:
        numero = int(input("Número do livro: "))  # ValueError se digitar letras

        if numero < 1 or numero > len(catalogo):
            print("⚠️ Número fora do intervalo.")
            return
        
        livro = catalogo[numero - 1]   # -1 porque lista começa em 0

        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            registrar_historico(livro["titulo"], "Emprestado")
            livro["disponivel"] = False
            print(f"✅ Empréstimo de '{livro['titulo']}' registrado.")
            salvar_catalogo(catalogo)

    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")



def devolver_livro(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return
    print("\n--- Registrar Devolução ---")

    try:
        numero = int(input("Número do livro a devolver: "))
        livro  = catalogo[numero - 1]  # IndexError se número for negatino ou > len

        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponivel.")
        else:
            registrar_historico(livro["titulo"], "Devolvido")
            livro["disponivel"] = True
            print(f"✅ Devolução de '{livro['titulo']}' registrada.")
            salvar_catalogo(catalogo)

    except ValueError:      # usamos os dois excepts separados ao invés de Exception, pois ele oculta todos os erros incluindo bugs do código
        print("❌ Digite apenas o número do livro.")
    except IndexError:
        print("❌ Número fora da lista. Verifique os livros cadastrados.")



def ver_historico(catalogo):
    """Lê o .txt e exibe o histórico de empréstimos e devoluções"""
    print("\n--- Histórico de Empréstimos e Devoluções ---")
    try:
        with open(HISTORICO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:           # ignora linhas vazias
                    continue
                partes = linha.split(SEPARADOR)
                livro, acao, data = partes
                print(f"  Livro: {livro} - {acao} em: {data}")
                
    except FileNotFoundError:
        pass    # primeira execução: arquivo ainda não existe - tudo bem
    return



def registrar_historico(livro, acao):
    """Registra todo empréstimo/devolução no arquivo historico.txt."""
    try:
        # 'a' = append: adiciona informações ao arquivo
        with open(HISTORICO, "a", encoding="utf-8") as f:
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            f.write(f"{livro}|{acao}|{data}\n")
    except IOError as e:
        print(f"❌ Erro ao registrar: {e}")



def contagem_historico():
    try:
        with open(HISTORICO, "r", encoding="utf-8") as f:
            livros_emprestados = []
            for linha in f:
                linha = linha.strip()
                if not linha:           # ignora linhas vazias
                    continue
                partes = linha.split(SEPARADOR)
                livro, acao, _ = partes
                if acao == "Emprestado":
                    print(livro)
                    livro = str(livro)
                    livros_emprestados.append(livro)
                
    except FileNotFoundError:
        pass    # primeira execução: arquivo ainda não existe - tudo bem
    return livros_emprestados



def relatorio(catalogo):
    total              = len(catalogo)
    disponiveis        = 0
    emprestados        = 0
    frequencia         = Counter(contagem_historico())
    mais_emprestado, _ = frequencia.most_common(1)[0]

    for livro in catalogo:
        if livro["disponivel"]:
            disponiveis += 1
        else:
            emprestados += 1

    print("\n--- Relatório de Acervo ---")
    print(f"📚 Total de livros       : {total}")
    print(f"✅ Livros disponiveis    : {disponiveis}")
    print(f"❌ Livros emprestados    : {emprestados}")
    print(f"📘 Livro mais emprestado : {mais_emprestado}")



def menu():
    # Carrega do arquivo ao iniciar - memória persistente
    catalogo = carregar_catalogo()
    total = len(catalogo)
    print(f"\n📚 SISTEMA DE BIBLIOTECA - v2 (com persistência)")
    print(f"    {total} livro(s) carregado(s) de '{ARQUIVO}'.")

    opcoes = {
        "1": ("Listar livros",          listar_livros),
        "2": ("Adicionar livro",        adicionar_livro),
        "3": ("Buscar livro",           buscar_livro),
        "4": ("Registrar empréstimo",   registrar_emprestimo),
        "5": ("Devolver livro",         devolver_livro),
        "6": ("Ver histórico",          ver_historico),
        "7": ("Relatório",              relatorio),
        "0": ("Sair",                   None),
    }

    while True:
        print("\n  Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")

        try:
            escolha = input("\n  Sua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")
            
        except ValueError as e:
            print(f"⚠️  {e}")
            continue            # volta ao while - não executa else/finally abaixo

        else:
            # Executando SOMENTE quando try termina sem exceção
            if escolha == "0":
                print("\n  Até logo: 📚")
                break
            _, funcao = opcoes[escolha]
            funcao(catalogo)                # passa o catalogo como argumento



if __name__ == "__main__":
    menu()
