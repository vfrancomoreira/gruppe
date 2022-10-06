"""
Escopo de variáveis

Dois casos de escopo:

1- Variáveis Globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2- Variáveis Locais:
    - Variáves locais, são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
     está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

 Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos um valor a mesma.

Exemplo C:
int numero = 42

Exemplo Java:
int numero = 42


"""

numero = 42  # Exemplo de variável global.
print(numero)
print(type(numero))

numero = 'Vinícius'
print(numero)
print(type(numero))

numero = 42
# novo = 0

if numero > 10:  # A variável "novo" está declarada localmente dentro do bloco if. Portanto é local.
    novo = numero + 10
    print(novo)
print(novo)