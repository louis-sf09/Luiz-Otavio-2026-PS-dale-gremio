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

    def __init__(self, nome, especie, idade, peso, vacinado, dataIn, dataOut):
        self.nome      = nome
        self.especie   = especie
        self.idade     = int(idade)
        self.peso      = float(peso)
        self.vacinado  = vacinado
        self.dataIn    = dataIn
        self.dataOut   = dataOut
        self.hospedado = True

    def exibir(self):
        print(f" Nome: {self.nome}")
        print(f" Espécie: {self.especie}")
        print(f" Hospedado: {"Sim" if self.hospedado else "Não"}")

    def emitir_resumo(self):
        print("--- Resumo do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Vacinado: {self.vacinado}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        print(f"Valor da diária: {self.calcular_diaria()}")
        print(f"Check-in : {self.dataIn}")
        print(f"Check-Out: {self.dataOut}")

    def registrar_entrada(self):
        if self.hospedado:
            print(f"\n{self.nome} já está no hotel.")
        else:
            self.hospedado = True
            self.dataIn    = datetime.now().strftime("%d/%m/%Y")
            self.dataOut   = "A definir..."
            print(f"\n{self.nome} entrou no hotel.")

    def registrar_saida(self):
        if self.hospedado:
            self.hospedado = False
            self.dataOut   = datetime.now().strftime("%d/%m/%Y")
            print(f"\n{self.nome} saiu do hotel.")
        else:
            print(f"\n{self.nome} já está fora do hotel")

    def atualizar_peso(self, novoPeso):
        self.peso = novoPeso
        print(f"\nPeso Atualizado com Sucesso! Novo peso de {self.nome}: {self.peso}")

    def calcular_diaria(self):
        if self.idade < 4:
            return int(50 + self.peso * 1.2)
        elif self.idade < 11:
            return int(60 + self.peso * 1.2)
        else:
            return int(70 + self.peso * 1.2)

    def para_linha_txt(self):
        return f"{self.nome};{self.especie};{self.idade};{self.peso};{self.vacinado};{self.dataIn};{self.dataOut};{self.hospedado}"


# ====================================================
# PERSISTÊNCIA EM TEXTO (.txt)
# ====================================================

def salvar_em_txt(pets, caminho):
    """Grava cada contato como uma linha no arquivo de texto."""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in pets:
            arquivo.write(c.para_linha_txt() + "\n")
    print(f"✅ {len(pets)} pet(s) salvo(s) em {caminho}")

# ====================================================
# PERSISTÊNCIA BINÁRIA (pickle)
# ====================================================

def salvar_em_binario(pets, caminho):
    """Serializa a lista inteira de pets de formato binário."""
    with open(caminho, "wb") as arquivo:
        pickle.dump(pets, arquivo)
    print(f"✅ {len(pets)} pet(s) salvo(s) em {caminho}")


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
    nome      = input("Nome : ")
    especie   = input("Espécie: ")
    idade     = input("Idade : ")
    peso      = input("Peso : ")
    vacinado  = input("Vacinado: ")
    dataIn    = datetime.now().strftime("%d/%m/%Y")
    dataOut   = "A definir..."
    pets.append(Pet(nome, especie, idade, peso, vacinado, dataIn, dataOut))
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
    numero = input("\nN° do pet a remover: ")
    cond, indice = digito(numero)
    if cond and 0 <= indice < len(pets):
        removido = pets.pop(indice)
        print(f"✅ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")


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


def resumo(pets):
    """Mostra a lista, pede um número e emite o resumo do pet escolhido."""
    listar(pets)
    if not pets:
        return
    numero = input("\nN° do pet para emitir o resumo: ")
    cond, indice = digito(numero)
    if cond and 0 <= indice < len(pets):
        pets[indice].emitir_resumo()
    else:
        print("Índice inválido.")


def buscar(pets):
    """Possibilita a busca de um pet por nome."""
    print("\n--- Buscar pet por nome ---")
    nome = input("Digite o nome do pet (ou o começo): ")
    nome = nome.lstrip()
    nome = nome.rstrip()
    c    = len(nome)
    resultados = [p for p in pets if p.nome[:c].lower() == nome.lower()]
    if resultados:
        for i, pet in enumerate(resultados, start=1):
            print(f"\n[{i}]")
            pet.emitir_resumo()
    else:
        print("(nenhum pet encontrado)")


def relatorio(pets):
    """Exibe apenas os pets hospedados."""
    print("\n--- Pets hospedados ---")
    i = 0
    for pet in pets:
        if pet.hospedado:
            i += 1
            print(f"\n[{i}]")
            pet.emitir_resumo()
    if i == 0:
        print("(nenhum pet hospedado)")


def digito(numero):
    if numero.isdigit():
        return True, int(numero) - 1
    else:
        return False, "_"


# ====================================================
# MENU PRINCIPAL
# ====================================================

def menu():
    pets = carregar_de_binario("hotel_pets.bin")
    while True:

        print("\n--- Hotel para Pets v2.0 ---\n")
        print(" 1. Cadastrar Pet")
        print(" 2. Listar Pets")
        print(" 3. Check-in")
        print(" 4. Check-out")
        print(" 5. Atualizar peso")
        print(" 6. Emitir resumo individual")
        print(" 7. Buscar por nome")
        print(" 8. Relatório de hospedados")
        print(" 9. Salvar em txt")
        print("10. Salvar em binário")
        print(" 0. Sair")
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
        elif opcao == "6":
            resumo(pets)
        elif opcao == "7":
            buscar(pets)
        elif opcao == "8":
            relatorio(pets)
        elif opcao == "9":
            salvar_em_txt(pets, "hotel_pets.txt")
        elif opcao == "10":
            salvar_em_binario(pets, "hotel_pets.bin")
        elif opcao == "0":
            salvar_em_binario(pets, "hotel_pets.bin")
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


# ====================================================
# PONTO DE ENTRADA
# ====================================================

if __name__ == "__main__":
    menu()
