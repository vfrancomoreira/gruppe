"""
Módulos customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python pronto para serem utilizados.

# Importando uma função específica
from funcao_com_parametro import soma

print(soma([4, 4]))


"""

# Importando todo módulo (Temos acesso a todos os elementos do módulo)
import funcao_com_parametro as fun_c_par

print(fun_c_par.lista)
print(fun_c_par.tupla)

print(fun_c_par.soma(fun_c_par.tupla))
