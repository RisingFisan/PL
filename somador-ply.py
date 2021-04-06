""" aula5: 2021-03-23

calclex.py
    - tokenizer
    in: (34-7)*2+3/2
    out: PA NUM SUB NUM PF MUL NUM ADD NUM DIV NUM


"""

import ply.lex as lex
import sys

tokens = (
    'ON','OFF',
    'DIG','EQ'
)

def t_ON(t): 
    r'[oO][nN]'
    t.lexer.semaforo = True

def t_OFF(t):
    r'[oO][fF]{2}'
    t.lexer.semaforo = False

def t_DIG(t):
    r'\d+'
    if t.lexer.semaforo: t.lexer.soma += int(t.value)

def t_EQ(t):
    r'='
    print("Soma =", t.lexer.soma)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.semaforo = True
lexer.soma = 0

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)