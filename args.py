"""
Entendendo o *args

- O *agrs é um parâmetro como outro qualquer. Isso significa que você
poderá chamar de qualquer coisa, desde que começe com asteristico.

Exemplo:

Poderiamos chamar este parâmetro de *xis, mas por convenção chamamos de *args

Mas oque é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imútaveis.

# Exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 6, 5))

# Entendendo o *args

def soma_todos_numeros(nome, sobrenome, *args):
    # Ou apenas utilizar: return sum(args)
    total = 0
    for n in args:
        total += n
    return total

print(soma_todos_numeros('Vinicius', 'Franco'))
print(soma_todos_numeros('Vinicius', 'Franco', 1))
print(soma_todos_numeros('Vinicius', 'Franco', 2, 3))
print(soma_todos_numeros('Vinicius', 'Franco', 2, 3, 4))
print(soma_todos_numeros('Vinicius', 'Franco', 3, 4, 5, 6))
print(soma_todos_numeros('Vinicius', 'Franco', 23.4, 12.5))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Eu não tenho certeza de quem você é'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))


def soma_todos_numeros(*args):
    return sum(args)

# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = 1, 2, 3, 4, 5, 6, 7

# num1, num2, num3, num4, num5, num6, num7 = numeros

# Desempacotador
print(soma_todos_numeros(*numeros))

# OBS: O asteristico serve para que informemos ao Python que estamos passando como argumento
# uma coleção de dados. Desta forma, ele saberá precisara antes desempacotar estes dados.
"""
