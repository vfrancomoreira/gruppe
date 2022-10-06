"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto
do mundo real, para a sua representação computacional, devemos poder criar
quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma classe
como variáveis do tipo definido na classe.

# Intância/Objetos
lamp1 = Lampada('Branca', 110, 60)

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Vinicius', 'Franco', 'vinicius@gmail.com', '123456')

nome = 'Vinícius'
sobrenome = 'Franco'
email = 'vinicius@gmail.com'
senha = '123456'

user = Usuario(nome, sobrenome, email, senha)
print(user)

print(type(42))

print('Geek')
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False

    def checa_lampada(self):
        return self.ligada

    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f"O cliente {self.__nome} diz oi!")

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cli1 = Cliente('Vinícius', '123.456.78-99')

cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz() # Jeito errado.
