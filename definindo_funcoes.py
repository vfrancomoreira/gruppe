"""
Definindo funções

- Funções são pequenas partes de código que realizam tarefas especificas.
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Elas são muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza varias tarefas dentro dela é bom fazer uma verificação
para que função seja simplificada.

Já ultilizamos várias funções desde que iniciamos este curso:

- print()
- len()
- max()
- min()
- count()
- E muitas outras;

"""

# Exemplo de ultilização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Ultilizando a função integrada (Built-in) do Python print()

# print(cores)

# curso = 'Programação em Python'

# print(curso)

# cores.append('roxo')

# print(cores)

# curso.append('Mais dados...')  # AttributeError
# print(curso)

# cores.clear()
# print(cores)

# print(help(print()))

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como definir funções?

"""
Em Python a forma geral de definir uma função é:

def nome_funcao(parametros_de_entrada):
    bloco_da_funcao


Onde:

nome_da_funcao -> Sempre com letras minúsculas, e se for nome composto, separado por underline (Snake Case);

parametros_de_entradas -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser
opcionais ou não; 

bloco_da_funcao -> Também chamado de corpo da função, ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função ultilizamos a palavra reservada 'def', informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com o já conhecido ':' que é ultilizado em Python para definir blocos.

"""


# Definindo a primeira função

# Definição

def diz_oi():
    print('Oi!')


"""
OBS:

1 - Veja que, dentro das nossas funções podemos ultilizar outras funções;
2 - Veja que, nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer 'Oi';
3 - Veja que, está função não recebe nenhum parâmetro de entrada;
4 - Veja que, está função não retorna nada;
"""

# Ultilizando funções

# Chamada de execução.

# diz_oi()

"""
ATENÇÃO: 

Nunca esqueça de ultilizar o parênteses ao executar uma função.

Exemplo:

# ERRADO
diz_oi 

# ERRADO
diz_oi ()

# CERTO
diz_oi()
"""

# Exemplo 2


def cantar_parabens():
    print('Parábens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


# for n in range(5):
#    cantar_parabens()

# Em Python podemos inclusive criar variáveis do tipo de uma função e executar essa função atráves da variável.

# Mas isso não é comum. O mais comum é chamá-la direto da função.

canta = cantar_parabens

canta()
