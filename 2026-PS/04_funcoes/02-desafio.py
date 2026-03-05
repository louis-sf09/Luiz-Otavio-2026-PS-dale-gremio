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
    print()

def exibir_rodape():
    """Mostra o rodapé do programa"""
    print()
    print("=" * 40)
    print("  SISTEMA ENCERRADO")
    print("=" * 40)

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



# ---- CÓDIGO PRINCIPAL ----
exibir_cabecalho()

nome  = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = calcular_media(nota1, nota2)

print()
print(f"Nota 1  : {nota1}")
print(f"Nota 2  : {nota2}")
print(f"Media   : {media}" )
print(f"Situação: {verificar_situacao(media)}")

exibir_rodape()
