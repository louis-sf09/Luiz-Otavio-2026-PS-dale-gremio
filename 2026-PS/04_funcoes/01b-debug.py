# Arquivo: 01b-debug.py

def saudacao(nome, turno="manhã"):      # Sem return -> retorna None
    mensagem = f"Boa {turno}, {nome}!"
    return mensagem

print(saudacao("Ana"))     # Retorno perdido -> não usa o retorno
print(saudacao("Bruno", "tarde"))

def dobrar(x):          # Sem return -> retorna None
    resultado = x * 2
    return resultado

print("Dobro  de 5:", dobrar(5))

total = 0
def incrementar():      # UnboundLocalError -> para alterar "total" a variável precisa ser global
    global total
    total = total + 1

incrementar()
print("Total:", total)

def contagem(n):        # RecursionError -> sem caso base, fica em um loop
    if n == 0:
        return
    print(n)
    contagem(n-1)

contagem(3)
