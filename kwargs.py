"""
**kwargs

Poderiamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla
o **kwargs exige que utilizemos parâmetros nomeados e transforma esses parâmetros extras em
um dicionário.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios

cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo

def comprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um comprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza de quem você é ...'

print(comprimento_especial())
print(comprimento_especial(geek='Python'))
print(comprimento_especial(geek='Oi'))
print(comprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter: (NESTA ORDEM)

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

def minha_funcao(nome, idade, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

minha_funcao('Julia', 8)
minha_funcao('Felicity', 18, 4, 5, 6, solteiro=True)
minha_funcao('Felipe', 34, eu='Não', voce='Vai')
minha_funcao('Carla', 19, 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração.

# Função com a ordem correta de parâmetros
# def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {sobrenome':'University', 'cargo':'Instrutor'}


# Função com a ordem incorreta de parâmetr  os
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

a = 1
b = 2
args = ()
3
kwargs = {sobrenome':'University', 'cargo':'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Vinícius', 'sobrenome': 'Franco'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
set = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set)

dicionario = dict(a=1, b=2, c=3, nome='Geek')

soma_multiplos_numeros(**dicionario)

# OBS! Os nomes das chaves de um dicionário devem ser os mesmos dos parâmetros da função.

# dicionario = dict(d=1, e=2, f=3) # TypeError
# soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Geek')

soma_multiplos_numeros(**dicionario, lang='Python')
"""

