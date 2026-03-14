# 05_modulos
Programa de conversão de unidades (temperatura, distância e massa) utilizando módulos, funções e pacotes.

## Estrutura de Arquivos
-> 05_modulos/              # Pasta geral do programa
    -> conversores/         # Pacote de módulos de conversão
        -> __init__.py      # API pública do pacote
        -> distancia.py
        -> massa.py
        -> temperatura.py
    -> debug_teste/         # Pasta de arquivo de debug
        -> 01b-debug.py
    -> utils/               # Pacote de módulos de formatação e validação
        -> __init__.py      # API pública do pacote
        -> formatador.py
        -> validador.py
    -> main.py              # Arquivo de execução do programa
    -> README.md            # Documentação

## Execução
Abra 2026-PS          [cd 2026-PS]
Abra 00_revisaoPython [cd 00_revisaoPython]
Abra 05_modulos       [cd 05_modulos]
Execute main.py       [python main.py]
Siga as instruções

## Módulos
-> Conversores:
    1. Distância: possui funções de conversão de distãncia(km, milhas, pés)
    2. Massa: possui funções de conversão de massa (kg, libras, gramas)
    3. Temperatura: possui funções de conversão de temperatura (celsius, fahrenheit, kelvin)
-> Utils:
    1. Formatador: possui funções para formatar as saídas do programa (cabeçalhos, linhas, resultados)
    2. Validador: possui função para validar a entrada do usuário (se é float, se está dentro de um limite)

## Exemplos
Você pode utilizar este programa para:
- Converter celsius para fahrenheit
- Converter quilogramas para libras
- Converter quilômetros para milhas

## Autoria
Desenvolvido por Luiz Otávio de Souza Freo, utilizando os códigos do Profe Berssa como base
