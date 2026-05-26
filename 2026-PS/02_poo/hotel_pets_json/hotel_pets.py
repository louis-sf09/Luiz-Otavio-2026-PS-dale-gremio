import json
import os

ARQUIVO_JSON = "pets.json"


class Pet:
    def __init__(self, nome, especie, raca, data, peso, altura, nome_dono, vacinado, hospedado=False):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.data = data
        self.peso = peso
        self.altura = altura
        self.nome_dono = nome_dono
        self.vacinado = vacinado
        self.hospedado = hospedado

    def exibir_dados(self):
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Raça: {self.raca}")
        print(f"Data de nascimento: {self.data}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura}")
        print(f"Dono: {self.nome_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def registrar_entrada(self):
        if self.hospedado:
            print(f"{self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registrar_saida(self):
        if not self.hospedado:
            print(f"{self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")

    def para_dicionario(self):
        """
        Transforma o objeto Pet em um dicionário.

        Isso é necessário porque o JSON não salva diretamente objetos Python.
        Ele salva dados simples: textos, números, booleanos, listas e dicionários.
        """
        return {
            "nome": self.nome,
            "especie": self.especie,
            "raca": self.raca,
            "data": self.data,
            "peso": self.peso,
            "altura": self.altura,
            "nome_dono": self.nome_dono,
            "vacinado": self.vacinado,
            "hospedado": self.hospedado
        }

    @staticmethod
    def criar_de_dicionario(dados):
        """
        Cria um objeto Pet a partir de um dicionário carregado do JSON.
        """
        return Pet(
            dados["nome"],
            dados["especie"],
            dados["raca"],
            dados["data"],
            dados["peso"],
            dados["altura"],
            dados["nome_dono"],
            dados["vacinado"],
            dados["hospedado"]
        )


def salvar_pets(lista_pets):
    """
    Salva a lista de objetos Pet no arquivo pets.json.
    """

    lista_dicionarios = []

    for pet in lista_pets:
        lista_dicionarios.append(pet.para_dicionario())

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)

    print("Dados salvos com sucesso em pets.json!")


def carregar_pets():
    """
    Carrega os pets do arquivo pets.json.

    Se o arquivo ainda não existir, retorna uma lista vazia.
    """

    if not os.path.exists(ARQUIVO_JSON):
        return []

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        lista_dicionarios = json.load(arquivo)

    lista_pets = []

    for dados in lista_dicionarios:
        pet = Pet.criar_de_dicionario(dados)
        lista_pets.append(pet)

    return lista_pets


def cadastrar_pet(lista_pets):
    print("\n--- Cadastro de Pet ---")

    nome = input("Nome do pet: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    data = input("Data de nascimento: ")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    nome_dono = input("Nome do dono: ")

    resposta = input("O pet está vacinado? (s/n): ").lower()
    vacinado = resposta == "s"

    pet = Pet(nome, especie, raca, data, peso, altura, nome_dono, vacinado)
    lista_pets.append(pet)

    print("Pet cadastrado com sucesso!")


def listar_pets(lista_pets):
    print("\n--- Lista de Pets ---")

    if not lista_pets:
        print("Nenhum pet cadastrado.")
        return

    for i, pet in enumerate(lista_pets, 1):
        print(f"\nPet {i}:")
        pet.exibir_dados()


def menu():
    pets = carregar_pets()

    while True:
        print("\n========= HOTEL PARA PETS =========")
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Salvar dados")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pet(pets)

        elif opcao == "2":
            listar_pets(pets)

        elif opcao == "3":
            listar_pets(pets)
            numero = int(input("Número do pet: "))
            pets[numero - 1].registrar_entrada()

        elif opcao == "4":
            listar_pets(pets)
            numero = int(input("Número do pet: "))
            pets[numero - 1].registrar_saida()

        elif opcao == "5":
            salvar_pets(pets)

        elif opcao == "0":
            salvar_pets(pets)
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
