"""
Try / Except / Else / Finally

Dica de quando e onde tratar o codígo:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor inválido.')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally.')

# Exemplo mais complexo ERRADO.

def div(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor está incorreto.')
try:
    print(div(num1, num2))
except TypeError:
    print('Tipo incorreto.')

# Exemplo mais complexo ERRADO.
# OBS: Você é responsavel pelas entradas das suas funções. Então, trate-as!


def div(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Tipo inválido'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero.'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(div(num1, num2))

# Exemplo mais complexo - Genérico.

def div(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema.'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(div(num1, num2))

# Exemplo mais complexo - Semi-Genérico.

def div(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o problema {err}.'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(div(num1, num2))

"""

