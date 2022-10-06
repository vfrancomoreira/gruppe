"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca serve para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando média dos dados utilizando a função mean()

media = statistics.mean(dados)

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.

# Forma de ler: Para cada 'valor' em 'dados.', o 'valor' tem que ser maior que a 'média'.
res = filter(lambda valor: valor > media, dados)
print(f'Os valores maiores que média: {media} são...')
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.
# print(f'Novamente:{list(res)}') Novamente:[]

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises)

# Forma 2
res = filter(lambda pais: len(pais), paises)

# Forma 3
res = filter(lambda pais: pais != '', paises)
print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto, filtrando apenas os elementos de acordo com a função.

# Exemplo mais complexo

usuarios = [
    {"USERNAME": "Samuel", "Tweets": ["Eu amo bolos", "Eu adoro pizza"]},
    {"USERNAME": "Carla", "Tweets": ["Eu amo meu gato"]},
    {"USERNAME": "Jeff", "Tweets": []},
    {"USERNAME": "Bob123", "Tweets": []},
    {"USERNAME": "Doggo", "Tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"USERNAME": "Gal", "Tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['Tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['Tweets'], usuarios))
print(inativos)

"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista 'Sua intrutora é' + nome, desde que cada nome tenha menos de 5 caracteres.

res = list(map(lambda nome: f'Sua intrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(res)
