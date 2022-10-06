"""
Dicionários

OSB: Em algumas linguagens de programação os dicionários Python são conheciodos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaver {}.

print(type({})

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos Comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos.

# Forma 1 - Acessando voa chave, da mesma forma que lista/tupla.

print(paises['br'])
# print(paises['ru'])

# Caso tentamos fazer acesso a uma chave que não existe teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None
e não será gerado KeyError.

pais = paises.get('ru'))

if pais:
    print(f'Encontrei o país {pais}.')
else:
    print('Não encotrei o país.')

# Podemos definir um valor padrão, para caso não encontremos o objeto com a frase informada.

pais = paises.get('ru', 'Não encontrado')
print(pais)

# Podemos verificar se determinada chave se encontra em um dicionário.

print('br' in paises)
print('ru' in paises)
print('eua' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário,
# como chaves de dicionários

# Tuplas por exemplo são bastante interessante de serem utilizadas como chaves de dicionários
# pois as mesmas são imutaveis

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário.

receita = {'Janeiro': 100, 'Fevereiro': 120, 'Março': 300}
print(receita)
print(type(receita))

# Forma 1 (Mais comum)

receita['Abril'] = 350
print(receita)

# Forma 2

novo_dado = {'Maio': 500}
receita.update(novo_dado)  # receita.update({'Maio': 500})
print(receita)

# Atualizando VALOR da CHAVE de um dicionário.

# Forma 1

receita['Maio'] = 550
print(receita)

# Forma 2

receita.update({'Maio': 600})
print(receita)

# CONCLUSÃO 1: A melhor forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'Janeiro': 100, 'Fevereiro': 120, 'Março': 300}
print(receita)

# Forma 1 (Mais comum)

ret = receita.pop('Março')
print(ret)
print(receita)

# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento o KeyError é retornado.
# OBS 2: Ao removermos um objeto o valor deste objeto é sempre retornado.

# Forma 2

del receita['Fevereiro']
print(receita)

# Se a chave não existir será gerado um KeyError.
# Neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preco;
    Produto 2:
        - nome;
        - quantidade;
        - preco;

# - Poderiamos utilizar uma Lista para isso? sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['GTA', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('GTA', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar um dicionário para isso? sim

carrinho = []

produto1 = {'nome': 'PlayStation4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'GTA', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário. (Zerar dados)

d.clear()
print(d)

# Copiando um dicionário para outro.

# Forma 1 - Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4
print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionários.

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nomes', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um interavel e um valor.
# ele vai gerar para cada valor do iteravel uma chave e irá atríbuir a está chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)