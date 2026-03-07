# ==============================================================
# CALCULADORA DE NOTAS
# ==============================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : Luiz Otávio de S. Freo
# Data       : 2026.03.05
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ==============================================================
#
# DESCRIÇÃO:
# Calcula as situações de aprovação de turmas,
# usando funções organizadas.
# ==============================================================

# ---- FUNÇÕES ----

def exibir_cabecalho():
    """Mostra o cabeçalho do programa"""
    print("=" * 40)
    print("  CALCULADORA DE NOTAS")
    print("=" * 40)

def exibir_rodape():
    """Mostra o rodapé do programa"""
    print()
    print("=" * 40)
    print("  SISTEMA ENCERRADO")
    print("=" * 40)

def solicitar_notas(nome_aluno):
    """Solicita e valida as notas do aluno"""
    nota1 = float(input(f"Digite a primeira nota do(a) {nome_aluno} (0 - 10): "))
    while nota1 < 0 or nota1 > 10:
        print("\nValor inválido! Digite uma nota entre 0 e 10")
        nota1 = float(input(f"Digite a primeira nota do(a) {nome_aluno} (0 - 10): "))
    
    nota2 = float(input(f"Digite a segunda nota do(a) {nome_aluno} (0 - 10): "))
    while nota2 < 0 or nota2 > 10:
        print("\nValor inválido! Digite uma nota entre 0 e 10")
        nota2 = float(input(f"Digite a segunda nota do(a) {nome_aluno} (0 - 10): "))
    
    return nota1, nota2

def calcular_media(nota1, nota2):
    """Calcula a média de um aluno usando 2 notas"""
    media = (nota1 + nota2) / 2
    return media

def verificar_situacao(media):
    """Verifica a situação de um aluno usando sua média"""
    if media >= 6.0:
        return "Aprovado"
    elif media >= 4.0:
        return "Recuperação"
    else:
        return "Reprovado"

def gerar_relatorio(nome, media, situacao):
    """Gera um relatório formado, claro e organizado"""
    print("-" * 40)
    print(f"Nome    : {nome}")
    print(f"Media   : {media:.2f}" )
    print(f"Situação: {situacao}")
    print("-" * 40)

def solicitar_medias_turma():
    """Solicita e valida uma das médias da turma"""
    media = float(input("Digite uma das médias da turma (0 - 10): "))
    while media < 0 or media > 10:
        print("\nValor inválido! Digite uma média entre 0 e 10")
        media = float(input("Digite uma das médias da turma (0 - 10): "))
    return media   

def resumo_turma(medias):
    """Calcula o total de alunos aprovados, em recuperação e reprovados"""
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for aluno in medias:
        if aluno >= 6.0:
            aprovados += 1
        elif aluno >= 4.0:
            recuperacao += 1
        else:
            reprovados += 1
    return aprovados, recuperacao, reprovados

def calcular_media_turma(medias):
    """Recebe a lista de medias da turma e calcula a media geral"""
    
    if len(medias) == 0:
        return 0

    media = medias[0]
    medias.pop(0)
    return media + calcular_media_turma(medias)



# ---- CÓDIGO PRINCIPAL ----
exibir_cabecalho()

# --- Desempenho individual de 3 alunos ---
print("\n--- Alunos ---\n")
for i in range(1, 4):       # repete 3 vezes (1 para cada aluno)
    nome         = input(f"Digite o nome do aluno {i}: ")
    nota1, nota2 = solicitar_notas(nome)
    media        = calcular_media(nota1, nota2)
    situacao     = verificar_situacao(media)
    print()
    gerar_relatorio(nome, media, situacao)

# --- Desempenho da turma ---
print("\n--- Turma ---\n")

# Leitura das médias da turma
medias = []
continuar = "s"
while continuar == "s":
    medias.append(solicitar_medias_turma())
    continuar = input("Adicionar média à turma? (s/n): ").lower()

# Calculo das situações dos alunos e da média geral
aprovados, recuperacao, reprovados = resumo_turma(medias)

qtd = len(medias)
media_turma = calcular_media_turma(medias) / qtd

# Relatório da turma
print("\n--- Relatório da Turma ---\n")
print(f"Total de alunos aprovados: {aprovados}")
print(f"Total de alunos em recuperação: {recuperacao}")
print(f"Total de alunos reprovados: {reprovados}")
print(f"Média geral: {media_turma:.2f}")

exibir_rodape()
