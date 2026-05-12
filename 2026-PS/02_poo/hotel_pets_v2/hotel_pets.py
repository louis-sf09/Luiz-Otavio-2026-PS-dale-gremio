# ====================================================
# Disciplina : Programação de Sistemas
# Aula       : 23 - Menu interativo e persistência de objetos
# Tipo       : Hotel para Pets v2.0
# Autor      : Luiz Otávio de Souza Freo
# Data       : 2026.05.07
# Descrição  : Sistema de Hotel para Pets que guarda os dados dos
#              pets e posui menu interativo para fazer alterações
# ====================================================

from datetime import datetime
import pickle

# ====================================================
# CLASSE Pet - representa cada pet cadastrado
# ====================================================

class Pet:
    """Representa um Pet do hotel"""

    def __init__(self, nome, peso, vacinado, data):
        self.nome      = nome
        self.peso      = peso
        self.vacinado  = vacinado
        self.data      = data
        self.hospedado = True

    def exibir(self):
        print(f" Nome     : {self.nome}")
        print(f" Peso     : {self.peso}")
        print(f" Vacinado : {self.vacinado}")
        print(f" Check-in : {self.data}")
        print(f" Hospedado: {"Sim" if self.hospedado else "Não"}")


# ====================================================
# PERSISTÊNCIA BINÁRIA (pickle)
# ====================================================

def salvar_em_binario(pets, caminho):
    """Serializa a lista inteira de pets de formato binário."""
    with open(caminho, "wb") as arquivo:
        pickle.dump(pets, arquivo)
    print(f"✅ {len(pets)} contato(s) salvo(s) em {caminho}")


def carregar_de_binario(caminho):
    """Lê o arquivo binário e devolve a lista de objetos pronta."""
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
        return []


# ====================================================
# CRUD EM MEMÓRIA
# ====================================================

def cadastrar(pets):
    """Lê os dados via input e adiciona um novo pet na lista."""
    print("\n--- Novo Pet ---")
    nome     = input("Nome : ")
    peso     = input("Peso : ")
    vacinado = input("Vacinado: ")
    data     = datetime.now().strftime("%d/%m/%Y")
    pets.append(Pet(nome, peso, vacinado, data))
    print("✅ Pet cadastrado.")


def listar(pets):
    """Mostra todos os pets cadastrados, numerados."""
    if not pets:
        print("\n(hotel vazio)")
        return
    print(f"\n--- Hotel para Pets v2.0 ({len(pets)} pets)---")
    for i, c in enumerate(pets, start=1):
        print(f"\n[{i}]")
        c.exibir()


def remover(pets):
    """Mostra a lista, pede um número e remove o pet escolhido."""
    listar(pets)
    if not pets:
        return
    indice = int(input("\nN° do pet a remover: ")) - 1
    if 0 <= indice < len(pets):
        removido = pets.pop(indice)
        print(f"✅ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")


# ====================================================
# MENU PRINCIPAL
# ====================================================

def menu():
    pets = carregar_de_binario("2026-PS/02_poo/hotel_pets_v2/hotel_pets.bin")
    while True:

        print("\n--- Hotel para Pets v2.0 ---\n")
        print("1. Cadastrar Pet")
        print("2. Listar Pets")
        print("0. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(pets)
        elif opcao == "2":
            listar(pets)
        elif opcao == "0":
            salvar_em_binario(pets, "2026-PS/02_poo/hotel_pets_v2/hotel_pets.bin")
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


# ====================================================
# PONTO DE ENTRADA
# ====================================================

if __name__ == "__main__":
    menu()
