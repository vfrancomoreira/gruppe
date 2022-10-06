"""
Levantando os próprios erros com raise

raise -> Lança exceções

OSB: raise não é uma função. É uma palavra reservada assim como def ou qualquer outra em Python.

Para simplificar, pense no raise sendo util para que possamos criar nossas próprias exeções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem do erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto não é string.')
    if type(cor) is not str:
        raise TypeError('O texto não é string.')
    print(f'O {texto} será impresso na cor {cor}.')

colore('minion', 'amarelo')

# Exemplo refatorado

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto não é string.')
    if type(cor) is not str:
        raise TypeError('O texto não é string.')
    if cor not in cores:
        print(f'A cor precisa ser entre:{cores}')
    print(f'O {texto} será impresso na cor {cor}.')

colore('minion', 'preto')

OBS: O raise assim como o return, finaliza a função, ou seja, nada após o raise é executado.

"""

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto não é string.')
    if type(cor) is not str:
        raise TypeError('O texto não é string.')
    if cor not in cores:
        print(f'A cor precisa ser entre:{cores}')
    print(f'O {texto} será impresso na cor {cor}.')

colore('minion', 'preto')
