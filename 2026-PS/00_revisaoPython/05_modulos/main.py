# ======================================================
# SISTEMA DE CONVERSÃO DE UNIDADES
# ======================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 07 - Revisão: Módulos
# Autor      : Luiz Otávio de S. Freo
# Data       : 2026.03.14
# Repositório: https://github.com/louis-sf09/Luiz-Otavio-2026-PS-dale-gremio
# ======================================================

# ---- Importação de pacotes e funções ----
from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes, kg_para_libras, kg_para_gramas
)
from utils import (
    cabecalho_secao, formatar_resultado, linha_separadora,
    validar_numero
)

# ---- Funções dos menus de cada conversão ----
def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    continuar = False
    while not continuar:
        valor = input("  Valor em C°: ")
        continuar, valor, msg_erro = validar_numero(valor)
        print(msg_erro)
    print(formatar_resultado("°C -> °F", valor, "°C", celsius_para_fahrenheit(valor), "°F"))
    print(formatar_resultado("°C -> K", valor, "°C", celsius_para_kelvin(valor), "K"))

def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    continuar = False
    while not continuar:
        valor = input("  Valor em km: ")
        continuar, valor, msg_erro = validar_numero(valor)
        print(msg_erro)
    print(formatar_resultado("km -> mi", valor, "km", km_para_milhas(valor), "mi"))
    print(formatar_resultado("km -> pés", valor * 1000, "m", metros_para_pes(valor * 1000), "pés"))

def menu_massa():
    print(cabecalho_secao("Conversão de Massa"))
    continuar = False
    while not continuar:
        valor = input("  Valor em kg: ")
        continuar, valor, msg_erro = validar_numero(valor)
        print(msg_erro)
    print(formatar_resultado("kg -> lbs", valor, "kg", kg_para_libras(valor), "lbs"))
    print(formatar_resultado("kg -> g", valor, "kg", kg_para_gramas(valor), "g"))

# ---- Função principal ----
def main():
    print(linha_separadora())
    print("  SISTEMA DE CONVERSÃO DE UNIDADES")
    print(linha_separadora())

    opcoes = {"1": menu_temperatura, "2": menu_distancia, "3": menu_massa}

    while True:
        print("\n [1] Temperatura  [2] Distância [3] Massa  [0] Sair")
        escolha = input("  Opção: ").strip()
        if escolha == "0":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("  Opção inválida.")

# ---- Chamada da Função principal ----
if __name__ == "__main__":
    main()
