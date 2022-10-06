"""
Módulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performace.

"""

# Fazer import

from collections import deque

# Criando deques

deq = deque('Geek')

print(deq)

# Adicionando elementos no deque

deq.append('Y')  # Adiciona no final.
print(deq)

deq.appendleft('K')  # Adiciona no começo da lista.
print(deq)

# Remover elementos

print(deq.pop())  # Remove e retorna o ultimo elemento.
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento.
print(deq)
