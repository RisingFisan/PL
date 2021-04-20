"""
linguagem dos parênteses:
()
((()))
()()()
()(())((()))()()

Par --> 
"""

import sys
import ply.yacc as yacc

from par_lex import tokens

def p_axioma(p):
    "S : Par"
    print(p[1])

def p_parentensis(p):
    "Par : PA Par PF Par"
    pass

def p_parentesis_empty(p):
    "Par : "
    pass

def p_error(p):
    print("Erro sintático:", p)
    parser.success = False

parser = yacc.yacc()

for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print("Frase válida:", linha)
    else:
        print("Frase inválida... Corrija e tente novamente")