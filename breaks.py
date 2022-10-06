"""
Saindo de loops com break

Funciona da mesma forma que C ou Java.

Ultilizamos o break para sair de loops de maneira projetada.

"""

#  Exemplo 1

for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print('Sair do loop.')

#  Exemplo 2

while True:
    comando = input("Digite 'Sair para sair:")
    if comando == 'sair':
        break
