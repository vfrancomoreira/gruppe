"""
Leitura de arquivos

Para ler o conteúdo de um arquivo em Python, ultilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada,
que neste caso é o caminho para o  arquivo a ser lido. Essa função retorna um _io.txtIOWrapper e é
com ele que trabalhamnos então.

OBS: Por padrão a função open() abre o arquivo para leitura. Esse arquivo deve existir,
ou então teremos o erro 'FileNotFoundError'.

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode 'r' = Modo leitura. r -> read() -> ler

"""

# Exemplo

arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura devemos utilizar o read()

ret = arquivo.read()
print(type(ret))
print(ret)

# print(arquivo.read())

# O Python utiliza o recurso para trabalhar com arquivos cursor. Esse cursor
# funciona como o cursor quando estamos escrevendo.

# print(arquivo.read())

# OBS: A função read() lê todo o conteúdo de um artquivo.
