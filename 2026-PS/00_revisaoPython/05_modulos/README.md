# 05_modulos
Programa de conversão de unidades (temperatura, distância e massa) utilizando módulos, funções e pacotes.

## Estrutura de Arquivos
- 05_modulos/              # Pasta geral do programa
    1. conversores/         # Pacote de módulos de conversão
        - __init__.py      # API pública do pacote
        - distancia.py
        - massa.py
        - temperatura.py
    2. debug_teste/         # Pasta de arquivo de debug
        - 01b-debug.py
    3. utils/               # Pacote de módulos de formatação e validação
        - __init__.py      # API pública do pacote
        - formatador.py
        - validador.py
    4. main.py              # Arquivo de execução do programa
    5. README.md            # Documentação

## Execução
1. Abra 2026-PS          [cd 2026-PS]
2. Abra 00_revisaoPython [cd 00_revisaoPython]
3. Abra 05_modulos       [cd 05_modulos]
4. Execute main.py       [python main.py]
5. Siga as instruções

## Módulos
- Conversores:
1. Distância: possui funções de conversão de distãncia(km, milhas, pés)
2. Massa: possui funções de conversão de massa (kg, libras, gramas)
3. Temperatura: possui funções de conversão de temperatura (celsius, fahrenheit, kelvin)
- Utils:
1. Formatador: possui funções para formatar as saídas do programa (cabeçalhos, linhas, resultados)
2. Validador: possui função para validar a entrada do usuário (se é float, se está dentro de um limite)

## Exemplos
Você pode utilizar este programa para:
- Converter celsius para fahrenheit
- Converter quilogramas para libras
- Converter quilômetros para milhas

## Autoria
Desenvolvido por Luiz Otávio de Souza Freo, utilizando os códigos do Profe Berssa como base
