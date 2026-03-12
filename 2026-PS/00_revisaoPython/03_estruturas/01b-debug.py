# Arquivo: 01b-debug.py

catalogo = [
    {"titulo": "Código Limpo",          "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python Fluente",        "autor": "Luciano Ramalho", "disponivel": True},
]

print("Primeiro livro:", catalogo[0]["titulo"])  # IndexError -> catalogo[3] não existe

print("\nLivros disponiveis:")
for livro in catalogo:
    if livro["disponivel"] == True:        # Erro lógico -> False é errado nesse caso
        print(f'  ✅ {livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo[0].items():    # TypeError -> sem .items()
    print(f"  {chave}: {valor}")

primeiro_autor = catalogo[0]["autor"]       # KeyError -> "Autor" não existe
print("\nAutor do primeiro livro:", primeiro_autor)
