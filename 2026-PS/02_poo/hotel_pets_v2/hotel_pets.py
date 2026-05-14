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

    def registrar_entrada(self):
        if self.hospedado:
            print(f"\n{self.nome} já está no hotel.")
        else:
            self.hospedado = True
            self.data = datetime.now().strftime("%d/%m/%Y")
            print(f"\n{self.nome} entrou no hotel.")

    def registrar_saida(self):
        if self.hospedado:
            self.hospedado = False
            print(f"\n{self.nome} saiu do hotel.")
        else:
            print(f"\n{self.nome} já está fora do hotel")

    def atualizar_peso(self, novoPeso):
        self.peso = novoPeso
        print(f"\nPeso Atualizado com Sucesso! Novo peso de {self.nome}: {self.peso}")


# ====================================================
# PERSISTÊNCIA EM TEXTO (.txt)
# ====================================================

def salvar_em_txt(pets, caminho):
    """Grava cada contato como uma linha no arquivo de texto."""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in pets:
            arquivo.write(c.para_linha_txt() + "\n")
    print(f"✅ {len(pets)} contato(s) salvo(s) em {caminho}")


def carregar_de_txt(caminho):
    """Lê o arquivo de texto e RECONSTRÓI os objetos Contato."""
    pets = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                nome, telefone, email = partes[0], partes[1], partes[2]
                pets.append(Pet(nome, telefone, email))
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
    return pets

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


def check_in(pets):
    """Mostra a lista, pede um número, e faz o check-in do pet escolhido."""
    listar(pets)
    if not pets:
        return
    numero = input("\nN° do pet para fazer o check-in: ")
    cond, indice = digito(numero)
    if cond and 0 <= indice < len(pets):
        pets[indice].registrar_entrada()
    else:
        print("Índice inválido.")


def check_out(pets):
    """Mostra a lista, pede um número, e faz o check-out do pet escolhido."""
    listar(pets)
    if not pets:
        return
    numero = input("\nN° do pet para fazer o check-out: ")
    cond, indice = digito(numero)
    if cond and 0 <= indice < len(pets):
        pets[indice].registrar_saida()
    else:
        print("Índice inválido.")


def atualizar(pets):
    """Mostra a lista, pede um número e atualiza o peso do pet escolhido."""
    listar(pets)
    if not pets:
        return
    numero = input("\nN° do pet para atualizar o peso: ")
    cond, indice = digito(numero)
    if cond and 0 <= indice < len(pets):
        novoPeso = float(input("Novo peso do pet: "))
        pets[indice].atualizar_peso(novoPeso)
    else:
        print("Índice inválido.")


def remover(pets):
    """Mostra a lista, pede um número e remove o pet escolhido."""
    listar(pets)
    if not pets:
        return
    numero = input("\nN° do pet a remover: ")
    cond, indice = digito(numero)
    if cond and 0 <= indice < len(pets):
        removido = pets.pop(indice)
        print(f"✅ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")

def digito(numero):
    if numero.isdigit():
        return True, int(numero) - 1
    else:
        return False, "_"


# ====================================================
# MENU PRINCIPAL
# ====================================================

def menu():
    pets = carregar_de_binario("2026-PS/02_poo/hotel_pets_v2/hotel_pets.bin")
    while True:

        print("\n--- Hotel para Pets v2.0 ---\n")
        print("1. Cadastrar Pet")
        print("2. Listar Pets")
        print("3. Check-in")
        print("4. Check-out")
        print("5. Atualizar peso")
        print("0. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(pets)
        elif opcao == "2":
            listar(pets)
        elif opcao == "3":
            check_in(pets)
        elif opcao == "4":
            check_out(pets)
        elif opcao == "5":
            atualizar(pets)
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
