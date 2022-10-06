"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i < 10; i++) {
    // execução do loop
}

Python

for item in interavel:
    // execução do loop

Ultilizamos loops para interar sobre sequências ou sobre valores iteraveis

Exemplo de iteráveis:
- String
    nome = 'Vinícius Franco'
- Lista
    lista = (1, 2, 5, 7, 9)
- Range
    numeros = range(1, 10)

# Exemplos de for 1 (Iterando sobre uma string)

# 'Para' cada 'letra' 'dentro' desse 'iteravel'
for letra in nome:
    print(letra)  # Mostre na tela a letra

# Exemplos de for 2 (Iterando sobre uma lista)

for numero in lista:
    print(numero)

# Exemplos de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'V'), (1, 'i'), (2, 'n'), (1, 'í')...)

for i, n in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo ultilizando um undeline (_)

nome = 'Vinícius Franco'
lista = (1, 2, 5, 7, 9)
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)


qtd = int(input("Quantas vezes esse loop deve rodar ?:"))

soma = 0

for n in range(1, qtd):
    num = int(input(f"Informe o {n} / {qtd}Valor:"))
    soma = soma + num
print(f"A soma é {soma}")

nome = 'Vinícius Franco'

for letra in nome:
    print(letra, end="")

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: U+F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
