"""
Listas (list)

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays

    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python

    - DINÂMICO: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente adicionando elementos;
    - QUALQUER tipo de dado: A listas possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representada por colchetes: []

Listas são mutaveis, ou seja, elas podem mudar constantemente.

type([])

lista1 = [1, 99, 4, 33, 2, 1, 44, 42, 27]

lista2 = ["V", "i", "n", "í", "c", "i", "u", "s"]

lista3 = []

lista4 = list(range(11))

lista5 = list('Vinícius')

#  Podemos facilmente checar se determinado valor está contido na lista

num = 18

if num in lista4:
    print(f"Encontrei o número {num}.")
else:
    print(f"Não encontrei o número {num}.")

#  Podemos facilmente ordenar uma lista.

lista1.sort()
print(lista1)

#  Podemos facilmente contar o número de ocorrências de um valor e uma lista.

print(lista1.count(1))

print(lista5.count('i'))

#  Adicionar elementos em listas.
#  Para adicionar elementos ou valores em listas ultilizamos a função append.
#  OBS: Com append nós só conseguimos adicionar 1 elemento por vez.
#  EX: lista1.append(12, 34, 50) ERRO


print(lista1)
lista1.append(43)
print(lista1)

lista1.append([8, 3, 1])  # Coloca a lista como elemento único. (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista.")
else:
    print("Não encontrei a lista")

lista1.extend([23, 34, 55])  # Coloca cada elemento como valor adicional a lista.
print(lista1)

#  Podemos inserir um novo elemento na lista informando a posição do indice.
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

#  Podemos facilmente juntar as duas listas.

#  lista6 = lista1 + lista5
lista1.extend(lista5)  # Tanto faz se você queira usar o + ou o extend.

print(lista6)

# Podemos facilmente inverter uma lista.

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()

print(lista6)

# Podemos contar quantos elementos existem dentro da lista.

print(len(lista2))

# Podemos remover facilmente o ultimo elemento de uma lista.
# OBS: O pop não somente remove o ultimo elemento mas tbm o retorna.

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice.
# OBS: Os elementos a direita deste indice serão deslocados para a esquerda.
# OBS: Se não houver elemento no indice informado, teremos o erro IndexError.

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)

print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista.

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista.

# Exemplo 1

nome = "Vinícius Franco dos Santos Moreira"
print(nome)
nome = nome.split()
print(nome)

# OBS: Por padrão o split separa o elemento da lista pelo espaço entre elas.

# Exemplo 2

nome = 'Vinícius,Franco,dos,Santos,Moreira'
print(nome)
nome = nome.split(',') # Aqui a gente fala pro split que o separador é a virgula
print(nome)


# Convertendo uma lista em uma string

lista6 = ['Progamando', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string.

nome = ' '.join(lista6)
print(nome)

# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string.

nome = '$'.join(lista6)
print(nome)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturanto esses dados.

lista6 = [1, 2.34, True, 'Vinícius', 'd', [1, 2, 3], 45616564]
print(lista6)
print(type(lista6))


# Iterando sobre listas.

# Exemplo 1 - Ultilizando for

soma = 0  # Para fazer a soma de string só trocar o 0 por ' '.

for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Ultilizando while

carrinho = []
produto = []

while produto != 'Sair':
    print("Adicione um produto na lista ou digite 'Sair' para sair")
    produto = input()
    if produto != 'Sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Ultilizando variaveis

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros1 = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de formas indexadas

#           0        1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Podemos fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense como um circulo, onde
# o final de um elemento está ligado ao inicio da lista.

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # ERRO, pois não existe indice -5

for cor in cores:
    print(cores)

indice = 0
while indice < len(cores):  # Enquando indice for menor que o número de cores
    print(cores[indice])  # Imprima pra mim CORES na POSIÇÃO indice.
    indice += 1  # indice + 0 + 1... até chegar o números de cores

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceita valores repetidos

lista = []

lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros metodos não tão importantes mas também úteis.

# Encontrar o indice de um elemento na lista..

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista está o valor 6 ?
print(numeros.index(6))

# Em qual indice da lista está o valor 9 ?
print(numeros.index(9))

# print(numero.index(19)) # Gera ValueErro.

# OBS: Caso não tenha este elemento na lista será apresentado ValueErro.

# OBS: Retorna o indice do primeiro elelemento encontrado.
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar e buscar.
print(numeros.index(5, 1))  # Buscando a partir do 1
print(numeros.index(5, 2))  # Buscando a partir do 2
print(numeros.index(5, 3))  # Buscando a partir do 3
# print(numeros.index(5, 1))  # Buscando a partir do 4
# OBS: Caso não tenha este elemento na lista será apresentado ValueErro.

# Podemos fazer busca entre dentro de um range, inicio/fim.

print(numeros.index(8, 3, 6))  # Buscar indice do valor entre indice 3 e 6.

# Revisão de slicing

# lista [inicio:fim:passo]
# range [inicio:fim:passo]

# Trabalhando com slice de listas com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])  # Iniciando no índice 1 e pegando todos elementos restantes.

# Trabalhando com slice de listas com o parametro 'fim'

print(lista[:2])  # Começa em 0 e pega o indice 2 - 1

print(lista[:4])  # Começa em 0 e pega o indice 4 - 1

print(lista[1:3])  # Começa em 1 e pega o indice 3 - 1

# Trabalhando com slice de listas com o parametro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2.

print(lista[::2])  # Começa em 0, vai até o final, de 2 em 2.

nomes = ['Vinícius', 'Franco']
nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Vinícius', 'Franco']
nomes.reverse()
print(nomes)

# Soma*, Valor Maximo*, Valor Minímo*, Tamanho.

# *Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4]

print(sum(lista))  # Soma
print(max(lista))  # Maxímo valor
print(min(lista))  # Minímo valor
print(len(lista))  # Tamanho da lista

# Transformar uma lista em tupla.

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError.


# Copiando uma lista para outra. (Shallow Cpy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que ao ultilizarmos a lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente idependentes, ou seja, modificando uma lista, não afeta a outra. Isso em python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shellow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar a modificação em uma das listas essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shellow Copy.

"""
