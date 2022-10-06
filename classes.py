"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle da lâmpadas da sua casa.

Classes pode conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente o testados de um objeto. No caso da lâmpada, possivelmente iríamos querer saber se a
    lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto
    pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito
    provavelmente iríamos querer representar no nosso sistema é o de desligar e desligar a mesma.

Em Python para definir uma classe, utilizamos a palavra reservada 'class'.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está
implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúsculo,
se o nome for composto utiliza-se a iniciais de ambas palavras em maiúsculo, todas juntas.

Dica: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para
nomes de classes, atributos, metodos, arquivos, diretórios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade.

"""


class Lampada:
    pass


lam = Lampada()
