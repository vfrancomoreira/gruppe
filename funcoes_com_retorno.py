"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}')

OBS: Em Python quando uma função não retorna nenhum valor o retorno é None.

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavrar reservada return.

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
Podemos passar a execução da função para outras funções.

# Vamos refaturar essa função para que ela retorne o valor.

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função.
ret = quadrado_de_7()
print(f'Retorno {ret}.')

print(f'Retorno {quadrado_de_7()}.')

# Refaturando a primeira função.

def diz_oi():
    return 'Oi '

alguem = 'Vinícius!'

print(diz_oi() + alguem)

OBS: Sobra a palavra reservada 'return'

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns;

def nova_funcao():
    var = True
    if var:
        return 4
    elif var is None:
        return 3.2
    return 'b'

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado até mesmo múltiplos valores;

def outra_funcao():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())

# Erros comuns na ultilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def e_impar():
    num = 5
    if num % 2 != 0:
        return True
    else:
        return False

print(e_impar())

# Não precisa do 'else'.
"""
