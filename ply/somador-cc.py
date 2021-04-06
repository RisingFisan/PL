""" aula5: 2021-03-23

calclex.py
    - tokenizer
    in: (34-7)*2+3/2
    out: PA NUM SUB NUM PF MUL NUM ADD NUM DIV NUM


"""

import ply.lex as lex
import sys

states = (
    ('semaforo','inclusive'),
)

tokens = (
    'ON', 'OFF',
    'PRINT', 'NUMBER'
)

def t_OFF(t):
    r'[oO][fF]{2}'
    t.lexer.begin('semaforo')

def t_NUMBER(t):
    r'\d+'
    t.lexer.soma += int(t.value)

def t_PRINT(t):
    r'='
    print("Soma =", t.lexer.soma)

t_ignore = ' \t'

def t_error(t):
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_semaforo_ON(t):
    r'[oO][nN]'
    t.lexer.begin('INITIAL')

def t_semaforo_NUMBER(t):
    r'\d+'
    t.lexer.skip(len(t.value))

lexer = lex.lex()

lexer.semaforo = True
lexer.soma = 0

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)