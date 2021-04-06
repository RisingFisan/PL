import ply.lex as lex
import sys

states = (
    ('comment','exclusive'),
)

tokens = ('CBEGIN', 'CEND', 'CONTENT')

def t_CBEGIN(t):
    r'/\*'
    t.lexer.begin('comment')

def t_CONTENT(t):
    r'.|\n'
    print(t.value, end='')

def t_comment_CEND(t):
    r'\*/'
    t.lexer.pop_state()

def t_ANY_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass

