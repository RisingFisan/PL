import ply.lex as lex

tokens = ['NUM', 'AP', 'FP', 'VIRG']

t_NUM = r'\d+'
t_AP = r'\['
t_FP = r'\]'
t_VIRG = r','

t_ignore = " \t\n"

def t_error(t):
    print("Caracter ilegal: " + t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    while linha := input():
        lexer.input(linha)
        for tok in lexer:
            print(tok)