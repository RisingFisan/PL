import ply.lex as lex

tokens = (
    'PA',
    'PF'
)

t_PA = r'\('
t_PF = r'\)'

def t_newline(t):
    r'\n+'
    pass

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")

lexer = lex.lex()
