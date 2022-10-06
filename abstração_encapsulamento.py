"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular -> Cápsula

               classe
-----------------------------------
|                                  |
|       atributos e métodos        |
|                                  |
-----------------------------------

# Relembrando Atributos/Métodos privados em Python

Imagige que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esse elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elento

Exemplo - Acessando elementos privados privados fora da classe;

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.

# Publico

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular} com limite {self.limite}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

# Testando

conta1 = Conta('Vinícius', 150.00, 1500)

# print(conta1.numero, conta1.titular, conta1.saldo, conta1.limite) Ou

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 350.00
conta1.limite = 1000.00

print(conta1.__dict__)

conta1.extrato()

# Privado

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)  #Name Mangling

conta1_Conta__titular = 'Angelina'

print(conta1.__dict__)

***** Continuação do privado

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite {self.__limite}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print("O valor deve ser positivo.")

    def transferir(self, valor, conta_destino):
        # 1- Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transferência paga por quem realizou a transferencia
        # 2- Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

# Testando


conta1 = Conta('Vinícius', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Cristina', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
