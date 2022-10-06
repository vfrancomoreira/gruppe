"""
Função com parâmetro

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada-> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saida;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refaturando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado()) # TypeError

# Refaturando a função

def cantar_parabens(aniversariante):
    print('Parábens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}')

cantar_parabens('Vinícius')

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplos

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(5, 5))
print(soma(10, 40))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError.

# print(soma(1, 2, 3)) # TypeError - Passando argumentos a mais.
# print(soma(4)) # TypeError - Passando argumentos a menos.

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Vinícius', 'Franco'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

# Erro comum na utilização do return - Colocar o return dentro do bloco do 'if'.

def soma_impares(numeros):
    total = 0
    for n in numeros:
        if n % 2 != 0:
            total = total + n
        return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))

"""


def soma(numeros):
    print(sum(numeros))


lista = [5, 5]
soma(lista)

tupla = (5, 5)
soma(tupla)
