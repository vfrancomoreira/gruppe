"""
Ranges
Precisamos conhecer o for para usar o ranges.
Precisamos conhecer o range para trabalhar melhor com os loops.
Ranges são ultilizado para gerar sequencias numéricas, não de formas aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive(inicio padrão 0 e passo 1 em 1)

# Exemplo Forma 1

for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive(inicio especificado pelo usuário e passo 1 em 1)

# Exemplo forma 2

for num in range(1, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(inicio especificado  pelo usuário, e passo especificado pelo usuário)

# Exemplo forma 3

for num in range(1, 10, 2): # Indo de dois em dois
    print(num)

# Forma 4 (Inversa)

range(inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(inicio especificado  pelo usuário, e passo especificado pelo usuário)

# Exemplo forma 4

for num in range(10, -1, -1): # Contagem regressiva
    print(num)

"""

for num in range(11):
    print(num)
