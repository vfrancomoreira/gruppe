"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução
do código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que
o Python não reconhece como parte da liguagem.

Exemplos SyntaxError

a)
def funcao:
    print('Geek University')

b)
def = 1

c)
return
    'return' outside function (A palavra return deve ser usada dentro de uma função).

2 - NameError -> Ocorre quando uma variável ou uma função não foi definida.

Exemplos NameError

a)
print(geek)

b)
geek()

c)
a = 15

# Para não gerar o erro, é possivel colocar uma variável global.
msg = 'algo'

if a < 10:
    msg = 'É menor que 10.'

print(msg)

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a)
print(len(5))

b) Concatenação
print('Geek' + [])
print('Geek' + 5) # solução é converter o número para uma string "print('Geek' + str(5))"

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.

Exemplos de IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

c)
tupla = ('Geek',)
print(tupla[2])

d)
tupla = ('Geek',)
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com o tipo correto
mas com o valor inapropriado.

Exemplos ValueError

a)
print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a)
dic = {}
print(dic['Geek'])

7 - AttribureError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttribureError

a)
tupla = (1, 55, 32, 7, 21)
tupla.sort() # sort(), ordena os números dentro da variável.
print(tupla) # Erro pelo fato da tupla ser imutavel, seria possivel apenas com a lista.

8 - IndetationError -> Ocorre quando não respeitamos a indentação do Pyhton (4 espaços)

Exemplos IndetationError

a)
def nova():
print('geek')

b)
for i in range(10):
i + 1

"""

