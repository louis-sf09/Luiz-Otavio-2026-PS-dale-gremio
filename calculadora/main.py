# Função da Soma
def soma(v1, v2):
    return(v1+v2)

# Função da Subtração
def sub(v1, v2):
    return(v1-v2)

# Função da Multiplicação
def mult(v1, v2):
    return(v1*v2)

# Função da Divisão
def div(v1, v2):
    return(v1/v2)

# Função para escrever o resultado
def escreva(msg, res):
    print(f"\nResultado:\n{msg} = {res}\n")

# Função principal do cálculo
def calc():
    sair = False

    while(sair==False):
        # Lê os 2 valores até que sejam números
        v1 = input("\nDigite o primeiro valor:\n")
        while(not v1.isnumeric()):
            print("\nDigite um valor válido!")
            v1 = input("Digite o primeiro valor:\n")

        v2 = input("Digite o segundo valor:\n")
        while(not v2.isnumeric()):
            print("\nDigite um valor válido!")
            v2 = input("Digite o segundo valor:\n")

        # Tranforma os valores em números
        v1 = int(v1)
        v2 = int(v2)

        # Lê a opção de operação até que seja válida
        ops = ["+", "-", "*", "/"]
        op = input("Digite a Operção [* / + -]:\n")
        while(op not in ops):
            print("Insira uma opção válida!")
            op = input("Digite a Operção [* / + -]:\n")

        # Calcula o resultado de acordo com a operação selecionada e mostra o resultado
        msg = f"{v1} {op} {v2}"

        if op=="+":
            res = soma(v1, v2)
            escreva(msg, res)
        elif op=="-":
            res = sub(v1, v2)
            escreva(msg, res)
        elif op=="*":
            res = mult(v1, v2)
            escreva(msg, res)
        elif op=="/":

            while(v2==0):
                print("Não é possível dividir por zero! Digite um divisor válido!")
                v2 = input("Digite o segundo valor:\n")
                
                while(not v2.isnumeric()):
                    print("Digite um valor válido!")
                    v2 = input("Digite o segundo valor:\n")
                v2 = int(v2)

            msg = f"{v1} {op} {v2}"
            res = div(v1, v2)
            escreva(msg, res)

        ops = ["S", "N"]
        op = input("Deseja sair?\n\n[S] Sim\n[N] Não\n\n")
        while(op not in ops):
            print("\nInsira uma opção válida!")
            op = input("Deseja sair?\n\n[S] Sim\n[N] Não\n\n")

        if (op=="S"):
            print("\nTchau!")
            break

# Chama a função principal
calc()
