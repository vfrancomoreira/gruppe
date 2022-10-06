"""
Utilizando Lambdas

Conhecida por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.

def soma(a,b)
    return a + b

# Função Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# title = ele deixa a primeira palavra maiúscula \ strip = remove os espaçamentos
print(nome_completo('Vinícius', 'FRANCO'))
print(nome_completo('  CRISTINA       ', 'franco'))

# Em função Python podemos ter nenhuma ou várias entradas. Em lambdas também

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x, y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ..., xn: <expressão> # Você pode inserir quantas entradas e expressões quiser.

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

# sort  = Usado no exemplo acima, irá ordenar os nomes pelo sobrenome.
# split = ''    ''   ''     ''  , irá separar por todos os espaços da variável autores.
# lower = ''    ''   ''     ''  , irá converter a palavra toda em minúscula.

print(autores)

"""

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """Retorna função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# Necessáriamente não precisaria de uma variável para a execução do gerador
print(geradora_funcao_quadratica(2, 3, -5)(2))
