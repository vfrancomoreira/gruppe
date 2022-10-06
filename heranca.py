"""
POO - Herança

Com a herança, a partir de uma classe existente, nós estendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente:
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario:
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

clente1 = Cliente('Vinícius', 'Franco dos Santos Moreira', '123.456.456.78', 5000)
funcionario1 = Funcionario('Cristina', 'Franco dos Santos', '456.123.789-89', 546)

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    '''Cliente herda de pessoa'''

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum
        self.__renda = renda


class Funcionario(Pessoa):
    '''Funcionario herda de pessoa'''

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma comum
        self.__matricula = matricula


clente1 = Cliente('Vinícius', 'Franco dos Santos Moreira', '123.456.456.78', 5000)
funcionario1 = Funcionario('Cristina', 'Franco dos Santos', '456.123.789-89', 546)

print(clente1.nome_completo())
print(funcionario1.nome_completo())

"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome {self._Pessoa__nome}'


clente1 = Cliente('Vinícius', 'Franco dos Santos Moreira', '123.456.456.78', 5000)
funcionario1 = Funcionario('Cristina', 'Franco dos Santos', '456.123.789-89', 546)

# Sobrescrita de métodos (overriding)

print(clente1.nome_completo())
print(funcionario1.nome_completo())
