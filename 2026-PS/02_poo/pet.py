'''
=================================================================
# ARQUIVO    : PET.PY
# Disciplina : Programação de Sistemas (2026-2)
# Aula       : Aula 20 - Por que POO?
# Autor      : Luiz Otávio de Souza Freo
# Conceitos  : Classe, objeto, atributos, métodos, encapsulamento
# Atividade  : Classe Pet
=================================================================
'''

from time import sleep

class Pet:
    '''
    Esta classe representa um Pet em um sistema simples de hotel para pets.

    Em vez de guardar os dados do pet em um dicionário solto, como fazíamos na programação estruturada, agora agrupamos os dados e comportamentos dentro de uma mesma classe.
    '''

    def __init__(self, nome, especie, idade, raca, peso, nome_dono, vacinado):
        '''
        Método construtor.

        Ele é executado automaticamente quando criamos um novo objeto Pet.

        Exemplo:
        pet1 = Pet("Rex", "Cachorro", 5)

        Parâmetros:
        - nome: nome do pet
        - especie: especie do pet
        - idade: do pet
        '''

        self.nome      = nome
        self.especie   = especie
        self.idade     = idade
        self.raca      = raca
        self.peso      = peso
        self.nome_dono = nome_dono
        self.vacinado  = vacinado
        self.hospedado = False

    def registrar_entrada(self):
        '''
        Registra a entrada do pet no hotel.

        Caso o Pet não esteja vacinado não poderá entrar no hotel

        Caso o Pet não esteja no hotel muda o atributo hospedado para True
        '''

        if self.vacinado:
            if self.hospedado:
                print(f"\n{self.nome} já está no hotel.")
            else:
                self.hospedado = True
                print(f"\n{self.nome} entrou no hotel.")
        else:
            print(f"\n{self.nome} precisa ser vacinado para entrar no hotel!")

    def registrar_saida(self):
        '''
        Registra a saída do pet do hotel.
        
        Se o pet estiver no hotel, muda o atributo hospedado para False
        '''

        if self.hospedado:
            self.hospedado = False
            print(f"\n{self.nome} saiu do hotel.")
        else:
            print(f"\n{self.nome} já está fora do hotel")

    def calcular_diaria(self):
        '''
        Calcula e retorna o valor da diária do pet.

        Valor recebe desconto baseado na idade do pet
        '''

        if self.idade < 4:
            return int(50 + self.peso * 1.2)
        elif self.idade < 11:
            return int(60 + self.peso * 1.2)
        else:
            return int(70 + self.peso * 1.2)

    def verificar_vacinacao(self):
        '''
        Verifica se o pet está vacinado.

        Se estiver emite "Vacinação em dia", caso não, emite "Atenção: vacinação pendente"
        '''

        if self.vacinado:
            print("\nVacinação em dia.")
        else:
            print("\nAtenção: vacinação pendente.")

    def atualizar_vacinacao(self):
        '''
        Atualiza a vacinação do pet.

        Se não estiver vacinado muda self.vacinado para True
        '''

        if self.vacinado:
            print(f"\n{self.nome} já está vacinado.")
        else:
            self.vacinado = True
            print(f"\n{self.nome} agora está vacinado.")

    def atualizar_peso(self):
        '''
        Atualiza o peso do pet.
        
        Exemplo: Peso antigo = 20 - atualizar_peso(28) - Peso novo = 28
        '''

        self.peso *= 1.2
        print(f"\nNovo peso de {self.nome}: {self.peso}")

    def emitir_resumo(self):
        '''
        Exibe um resumo geral do pet.
        
        Exemplo: Nome: Rex    Espécie: Cachorro    Idade: 5
        '''

        print("\n--- Resumo do Pet ---")
        print(f"Nome do pet:     {self.nome}")
        print(f"Espécie:         {self.especie}")
        print(f"Raça:            {self.raca}")
        print(f"Idade:           {self.idade}")
        print(f"Peso:            {self.peso}")
        print(f"Nome do dono:    {self.nome_dono}")
        print(f"Vacinado:        {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado:       {'Sim' if self.hospedado else 'Não'}")
        print(f"Valor da diária: {self.calcular_diaria()}")



'''
Testes da classe Pet

Criando objetos (pet1, pet2 ...) e testando os métodos da classe
'''

pet1 = Pet("Rex", "Cachorro", 5, "Labrador", 22.5, "Maria", True)
pet2 = Pet("Mimi", "Gato", 2, "Siamês", 4.2, "João", True)
pet3 = Pet("Thor", "Cachorro", 11, "Vira-lata", 18.0, "Ana", False)
pet4 = Pet("Nicolau", "Gato", 2, "Branco com laranja", 3.5, "Luiz", True)
pet5 = Pet("Antenor", "Cachorro", 12, "Vira-lata", 7.0, "Luiz", True)

pets = [pet1, pet2, pet3, pet4, pet5]

for i, pet in enumerate(pets):
    print(f"\n----- Pet {i+1} -----")
    pet.emitir_resumo()
    sleep(3)
    pet.verificar_vacinacao()
    sleep(3)
    pet.registrar_entrada()
    sleep(3)
    pet.atualizar_vacinacao()
    sleep(3)
    pet.registrar_entrada()
    sleep(3)
    pet.atualizar_peso()
    sleep(3)
    pet.emitir_resumo()
    sleep(3)
    pet.registrar_saida()
    sleep(5)
