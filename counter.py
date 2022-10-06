"""
Módulo Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High - Performance Container Datetypes

Counter -> Recebe um interável como um parâmetro e cria um objeto do tipo Collections Counter que é parecido
como um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar iterável, aqui utilizamos uma Lista.
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 45, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 2: 5, 3: 5, 4: 2, 5: 2, 45: 1, 66: 1, 43: 1, 34: 1})

# Veja que para cada elemento da Lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Vinícius Franco'))
# Counter({'i': 2, 'n': 2, 'c': 2, 'V': 1, 'í': 1, 'u': 1, 's': 1, ' ': 1, 'F': 1, 'r': 1, 'a': 1, 'o': 1})

# Exemplo 3

from collections import Counter

texto = Para todos os leitores e leitoras do Brasil,
Não deixe de ler isto. Nesta segunda-feira, pela primeira vez nos últimos tempos, pedimos humildemente
 que você defenda a independência da Wikipédia. Os 98% dos nossos leitores não doam. Eles não prestam
 atenção a este pedido. Se você doar apenas R$ 10, ou o que puder, a Wikipédia pode continuar crescendo. A
 maioria das pessoas doa porque a Wikipédia é útil. Ao doar R$ 10, você mostra aos editores que trazem informações
 neutras e verificadas que o trabalho deles é importante. Se você é um dos nossos raros doadores, somos
 imensamente gratos. Sua doação é importante.'

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto.
print(res.most_common(5))
"""


