"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap tupla

tupla = (1, 2, 3)
print(tupla[2])

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.

"""

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])  # Recomendada (Por ficar mais claro de entender)

# Usando

ray = cachorro(idade=2, raca='Bull Terrier', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0])  # Idade
print(ray[1])  # Raça
print(ray[2])  # Nome

# Forma 2 - Recomendada (Por ser mais fácil visívelmente de entender no código)

print(ray.idade)  # Idade
print(ray.raca)  # Raça
print(ray.nome)  # Nome

print(ray.index('Bull Terrier'))  # Qual indíce do valor.
print(ray.count('Bull Terrier'))  # Quantas ocorrências da raça tem na tupla.
