"""
Mapas -> Conhecidos em Python como dicionários.

Dicionários em Python são representados por chaves {}.

# Iterar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

# Acessando as chaves

print(receita.keys())

for chave in receita:
    print(chave)

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave} e Valor = {valor}')
"""

receita = {'Jan': 100, 'Fev': 250, 'Mar': 400}
print(receita)

# Soma*, ValorMáximo*, ValorMínimo*, Tamanho

# * Se os valores foram todos inteiros ou reais.

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
