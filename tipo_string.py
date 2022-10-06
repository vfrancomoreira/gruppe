"""
Tipo string

Em python, um dado considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.2'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.2"
- Estiver entre aspas simples tríplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.2'''
"""
# - Estiver entre aspas duplas tríplas -> """uma string""", """234""", """a""", """True""", """42.2"""
"""
nome = 'Vínicius Franco'
print(nome)
print(type(nome))

nome = "Vinícius Franco"
print(nome)
print(type(nome))

nome = "Vinícius \n Franco"
print(nome)
print(type(nome))

nome = "Vinícius
Franco" # aspas duplas triplas
print(nome)
print(type(nome))

nome = "Vinícius \" Franco"
print(nome)
print(type(nome))

print(nome.upper()) # Transforma tudo em maiúsculo.

print(nome.lower()) # Transforma tudo em tudo minúsculo.

print(nome.split()) # Transforma em lista de string.

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,    10,   11,   12,   13,  14 ]
# ['V', 'i', 'n', 'í', 'c', 'i', 'u', 's', ' ', 'F',  'r',  'a',  'n',  'c',  'o']
nome = 'Vinícius Franco'
print(nome[0:8])  # Slice de string

print(nome[9:15])  # Slice de string

# [     0    ,     1   ]
# ['Vinícius', 'Franco']
print(nome.split()[0])

print(nome.split()[1])

# [::-1] -> Comece do primeiro elemento vá até o último e inverta.
print(nome[::-1])  # Inversão de String Pythônico.

print(nome[14], nome[13])  # Inversão por uma letra de cada vez

print(nome.replace('V', 'B'))  # Inversão de letras

"""
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,    10,   11,   12,   13,  14 ]
# ['V', 'i', 'n', 'í', 'c', 'i', 'u', 's', ' ', 'F',  'r',  'a',  'n',  'c',  'o']
nome = 'Vinícius Franco'

texto = 'socorram me subino onibus em marrocos'
print(texto)

print(texto[::-1])