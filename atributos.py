"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de Instância: São atributos declarados dentro do método contrutor.

# OBS: Método contrutor é um método especial utilizado para a contrução do objeto.

# Em Java uma classe em Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private string cor;
    private Boolean ligada = false;
    public Lampada (int voltagem, String cor){
    this.voltagem = votagem;
    this.cor = cor
    }
}

# Em Python por convenção ficou estabelecido que todo atribut de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto.
Case queiramos demonstrar que determinado produto deve ser tratado como privado, ou seja.
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no ínicio de seu nome.

Isso é conhecido também como Name Mangling.

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '1234')

print(user.email)

# print(user.senha) # AttribuiteError

# print(user._Acesso__senha)  # Temos acesso, mas não deveríamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()

# O que significa atibutos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe todas as instâncias terão esses atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

# Atributos de Classe são atributos que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente inicializamos um valor e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao ínves de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe, todas as instâncias
# terão o mesmo valor para este atributo.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox Series', 'Video Game', 4300)

print(p1.valor)  # Acesso possível mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# Em linguagens como Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;


"""

# Classes com Atributos de Instância Públicos


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Publicos e Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Refatorar a classe atributo

class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05 de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.


p1 = Produto('PlayStation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso.

print(f'Produto: {p2.nome}. Descrição: {p2.descricao}. Peso: {p2.peso}. Valor:{p1.valor}.')
# print(f'Produto: {p1.nome}. Descrição: {p1.descricao}. Peso: {p2.peso}. Valor:{p1.valor}.')

# Acessando os dados da classe

# print(Produto.__dict__)

# Acessando dados do metodos

print(p1.__dict__)

# Deletando atributos

del p1.descricao
del p1.valor

print(p1.__dict__)
