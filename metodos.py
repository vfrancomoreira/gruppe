"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em dois grupos: Métodos de instância e Métodos de classe

# Métodos de instância

# O método dunder init __init__ é um método especial chamado de contrutor e
sua função é construir um objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas própias funções utilizando dunder (duplo underline no início e no fim)
não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportaento
dessas funções mágicas internas da linguagem. Então , evite ao máximo. De preferência NUNCA FAÇA.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá a as palavras separadas por underline.

p1 = Produto('PlayStation 4', 'Video Game', 2300)

print(p1.desconto(10))

print(Produto.desconto(p1, 10))  # self, desconto

user1 = Usuario('Vinícius', 'Franco', 'user1@gmail.com', '123456')
user2 = Usuario('Willian', 'Smith', 'user2@gmail.com', '654321')

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

print(f'Senha User1: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe
print(f'Senha User2: {user2._Usuario__senha}')  # Acesso de forma errada de um atributo de classe

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha inválida.')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # LEMBRANDO: Acesso errado

# Métodos de classe em Python são conhecidos como métodos estáticos em outras linguagens.

# Métodos de Classe

user = Usuario('Vinícius', 'Franco', 'vinicius@gmail.com', '1234')

Usuario.conta_usuario()  # Forma correta.

user.conta_usuario()  # Possível, mas incorreta.

user = Usuario('Vinicius', 'Franco', 'viniciuszica@gmail.com', '123456')

print(user._Usuario__gera_usuario()) # Acesso de forma ruim...

class Lampada:
    def __init__(self, cor, vantagem, luminosidade):
        self.__cor = cor
        self.__vantagem = vantagem
        self.__luminosidade = luminosidade
        self.lampada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        'Retorna o valor com desconto'
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


"""


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Vinícius', 'Franco', 'vinizica@gmail.com', '123456')

print(Usuario.contador)

print(Usuario.definicao())
