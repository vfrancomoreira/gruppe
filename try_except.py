"""
O bloco try/except

Utilizamos o bloco try/except para trata erros que podem ocorrer no nosso código.
Prevenindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inexperadas.

A forma geral mais simples é:

try: tradução (tente)
    //execução problemática
except:
    //o que deve ser feito em caso de problemas

# Exemplo 1

# Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2

# Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a melhor foma de tratamento de erros. O ideal é
sempre tratar de forma específica.

# Exemplo 3 - Tratando um erro específico.

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 4 - Tratando um erro específico.

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente.')

OBS: Para cada objeto é necessário identificar o tipo de erro, caso coloque um try diferente de
except dará erro.

# Exemplo 5 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez

try:
    print('geek'[5])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as erra:
    print(f'Deu NameError: {erra}')
except:
    print(f'Deu um erro diferente')

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Vinícius'}

print(pega_valor(dic, 'nome'))
