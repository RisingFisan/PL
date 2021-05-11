# Parser recursivo descendente, LL(1) para listas de inteiros

# p1: Lista -> '[' Cont
# p2: Cont -> ']'
# p3:       | Elementos ']'

# p4: Elementos -> num ContElem
# p5: ContElem -> vazio
# p6:           | ',' Elementos

"""
         | '[' | ']' | ',' | num |  $  | 
---------+-----+-----+-----+-----+-----+
Lista    | p1  | --- | --- | --- | --- |
Cont     | --- | p2  | --- | p3  | --- |
Elementos| --- | --- | --- | p4  | --- |
ContElem | --- | p5  | p6  | --- | --- |
"""

from lista_lex import tokens, lexer

prox_simb = None

def erro(esperado, recebido):
    print(f"Estava à espera de {esperado} e recebi {recebido}")

def rec_term(simbolo):
    global prox_simb
    if prox_simb == simbolo:
        prox_simb = get_simb()

def get_simb():
    try:
        return lexer.token().type
    except AttributeError:
        return None

def rec_lista():
    global prox_simb
    if prox_simb == 'AP':
        rec_term('AP')
        rec_Cont()
    else:
        erro('AP', prox_simb)

def rec_Cont():
    global prox_simb
    if prox_simb == 'FP':
        rec_term('FP')
    elif prox_simb == 'NUM':
        rec_Elementos()
        rec_term('FP')
    else:
        erro("FP ou NUM", prox_simb)

def rec_Elementos():
    global prox_simb
    if prox_simb == 'NUM':
        rec_term('NUM')
        rec_ContElem()
    else:
        erro("NUM", prox_simb)

def rec_ContElem():
    global prox_simb
    if prox_simb == 'FP':
        pass
    elif prox_simb == 'VIRG':
        rec_term('VIRG')
        rec_Elementos()
    else:
        erro("FP ou VIRG", prox_simb)

if __name__ == '__main__':
    while linha := input():
        lexer.input(linha)
        prox_simb = get_simb()
        rec_lista()

