"""
Loop while

Forma geral

while expressão_booleana
    //execuçãp do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

Exemplo:

num = 5

num < 10

True, porque numero é menor que 10.

# Exemplo 1

num = 0

while num < 10:
    num = num + 1
    print(num)

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar loop infinito.

# Exemplo 2

res = ''

while res != 'sim':
    res = input("Já acabou Jéssica ?")

"""
num = 0

while num < 10:
    num = num + 1
    print(num)
