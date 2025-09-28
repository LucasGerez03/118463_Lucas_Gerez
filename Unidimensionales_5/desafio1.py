import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from desafio_modulos.funciones import es_par_o_impar

es_par_o_impar(5)
