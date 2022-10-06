"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar listas com dados processados a partir de outro
iterável.

# Sintaxe da List Comprehension

[dado for dado in iterável]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)
"""
"""
Para entender melhor o que está acontecendo devemos dividir a espressão em duas partes:

- A primeira parte: for numero in numeros

- A segunda parte: numero * 10

ou

      [divida o numero por 2 para cada numero em numeros]
res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)

# List Comprehesions versos Loop

# Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrado = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrado.append(numero_dobrado)

print(numeros_dobrado)

# List Comprehesions

print([numero * 2 for numero in numeros])

"""

# Outros exemplos

# 1

nome = 'Vinícius'

print([letra.upper() for letra in nome]) # Todas letras maiúsculas.

# 2


def caixa_alta(nome): # Primeira letra maiúscula.
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor for valor in [0, [], '', True, 1, 3.14])])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
