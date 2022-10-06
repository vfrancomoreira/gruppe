"""
Estruturas lógicas: and(e), or(ou), not(não), is(é)

Operadores unirarios:
    * not;
Operadores bínarios:
    * and, or, is;

Regras de funcionamento:

Para 'and', ambos precisam ser True.
Para 'or', um ou outro precisa ser True.
Para o 'not', o valor do booleano é invertido, se for True, vira False, se for false vira True.
Para o 'is', o valor é comparado com um segundo. 1 ´é´ 1 = True / 1 == 1 True
"""

ativo = True
logado = False

if ativo:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar a sua conta. Por favor, cheque seu e-mail")

# ativo é True ?
print(ativo is True)