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
    nota1 = float(input(f"Digite a primeira nota do(a) {nome_aluno} (0 - 10)): "))
    while nota1 < 0 or nota1 > 10:
        print("\nValor inválido! Digite uma nota entre 0 e 10")
        nota1 = float(input(f"Digite a primeira nota do(a) {nome_aluno} (0 - 10)): "))
    
    nota2 = float(input(f"Digite a segunda nota do(a) {nome_aluno} (0 - 10): "))
    while nota2 < 0 or nota2 > 10:
        print("\nValor inválido! Digite uma nota entre 0 e 10")
        nota2 = float(input(f"Digite a segunda nota do(a) {nome_aluno} (0 - 10)): "))
    
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



# ---- CÓDIGO PRINCIPAL ----
exibir_cabecalho()

for i in range(1, 4):       # repete 3 vezes (1 para cada aluno)
    print()
    nome         = input(f"Digite o nome do aluno {i}: ")
    nota1, nota2 = solicitar_notas(nome)
    media        = calcular_media(nota1, nota2)
    situacao     = verificar_situacao(media)
    print()
    gerar_relatorio(nome, media, situacao)

exibir_rodape()
