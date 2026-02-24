# Arquivo: 01b-debug.py

nome = input("Digite o nome o aluno: ")     # Erro 1: SyntaxError -> ❌ "imput" -> ✅ "input"
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2       # Erro 2: Erro lógico -> são necessários os ()

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:                               # Erro 3: IndentationError
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}") # Erro 4: SyntaxError -> ❌ "pront" -> ✅ "print"
