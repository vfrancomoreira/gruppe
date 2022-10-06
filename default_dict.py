"""
Múdulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionários

dicionario = {'curso': 'Programação em Python'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # KeyError. (Erro de Chave)

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso temos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuído.

OSB: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada
e retornar valores.


"""

# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)  # Também é possivel inserir uma str no lugar do 0.

dicionario['curso'] = 'Programação em Python Essêncial'
print(dicionario)

print(dicionario['outro'])  # Teria KeyError em um dicionário comum, mas dessa forma não.

print(dicionario)
