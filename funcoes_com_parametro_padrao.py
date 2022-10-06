"""
Funções com parâmetro padrão (Defaut paramters)

- Funções onde a passagem de parâmetro seja opcional.

# Exemplo de função onde a passagem de parâmetro seja opcional.

print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3)) # Por padrão eleve ao quadrado.
print(exponencial(3, 5)) # Eleva a potência informada pelo usuário

# OBS: Se o usuário passar somente 1 argumento, este será atríbuido ao parâmetro numero, e será
# calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potência.
# Então será calculada a está potência.

print(exponencial())

# OBS: Em funções Python os parâmetros com os valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO !

def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) # TypeError - Porque aqui se torna obrigatório, pois nenhum valor foi atribuído no parâmetro.
print(soma()) # TypeError - Aqui também se torna obrigatório, pois nenhum valor foi atribuído no parâmetro.

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao(nome='Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Porque utilizar parâmetros com valor default?

- Nos permite ser mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permites trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar com valores default para parâmetros?

- Qualquer tipo de dados:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc...

# Exemplos: Funções como parâmetro.

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def sub(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, sub))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global.

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}.'

print(diz_oi())

# Se tivermos variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Geek' # Variável local
    return f'Olá {prof}'

print(diz_oi())
print(prof) # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!).

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

# ATENÇÃO com variáveis globais (Se puder evitar, evite!).

total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável gloval.
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável.

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

# print(dentro()) # NameError - Porque a função está 'dentro' da função 'fora'.
