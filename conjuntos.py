"""
Conjuntos
    - Conjuntos em qualquer linguagem de programação estamos fazendo referencia a
    Teoria dos Conjuntos da matemática.

- No Python os conjuntos são chamados de Sets.

Dito isto, da mesma forma que da matemática:
    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em Python com chaves. {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionário).
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.
print(s)
print(type(s))

# OSB: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erros e não fará parte do conjunto.

# Forma 2 (Mais comum)

n = 9

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto.

if n in s:
    print(f'Tem {n}.')
else:
    print(f'Não tem o {n}.')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem.

# Listas aceitam valores duplicados, então temos 10 elementos.
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista:      {lista} com {len(lista)} elementos.')

# Tuplas aceitam valores duplicados, então temos 10 elementos.
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla:      {tupla} com {len(tupla)} elementos.')

# Dicionários não aceitam chaves duplicados, então temos 8 elementos.
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], '')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos.')

# Conjunto não aceitam valores duplicados, então temos 8 elementos.
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Contunto:   {conjunto} com {len(conjunto)} elementos.')

# Assim como todo outro conjunto Python pordemos colocar todos os outros tipos de dados misturados em Sets.

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um Set normalmente.
for valor in s:
    print(valor)

# Usos interesantes com Sets.

# Imagine que fizemos um formulário de cadastros de visitantes em uma feira ou museu, e
# os vistitantes informaram manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, única, temos.

print(len(set(cidades)))

# Adicionando elementos em um conjunto.

s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplismente é ignorado e não é adicionado.
print(s)

# Remover elementos em um conjunto.

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  # Não é índice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(2)
print(s)

# OBS: Se o valor não for encontrado nenhum erro é gerado.

# Copiando um conjunto para outro.

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto.

s.clear()
print(s)

estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java) # Recomendado
# {'Marcos', 'Ana', 'Ellen', 'Julia', 'Fernando', 'Guilherme', 'Patrícia', 'Pedro', 'Gustavo'}
# unicos1 = estudantes_java.union(estudantes_python)
# {'Guilherme', 'Patrícia', 'Gustavo', 'Pedro', 'Ellen', 'Fernando', 'Ana', 'Marcos', 'Julia'}
print(unicos1)

# Forma 2 - Utilizando o caracterer pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#  Métodos matemáticos de conjuntos.

# Imagine que temos dois conjuntos: Um contendo estudanytes do cursos Python e um contendo
# estudantes do curso de java

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro.

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

# Soma*, ValorMáximo*, ValorMínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais.

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
