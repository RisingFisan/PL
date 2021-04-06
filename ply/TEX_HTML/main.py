import ply.lex as lex

states = (
    ('chapter','inclusive'),
    ('section','inclusive'),
    ('subsection','inclusive'),
    ('subsubsection','inclusive'),
    ('enumerate','inclusive'),
    ('itemize','inclusive'),
    ('item','inclusive'),
    ('bold','inclusive'),
    ('italics','inclusive'),
    ('underline','inclusive'),
)

tokens = (
    'CHAPTER',
    'SECTION',
    'SUBSECTION',
    'SUBSUBSECTION',
    'BOLD',
    'ITALICS',
    'UNDERLINE',
    'ENUMERATE',
    'ITEMIZE',
    'ITEM',
    'TEXT'
)

def t_CHAPTER(t):
    r'\\chapter\{'
    print("<h1>", end='')
    t.lexer.push_state('chapter')

def t_chapter_exit(t):
    r'\}'
    print("</h1>", end='')
    t.lexer.pop_state()

def t_SECTION(t):
    r'\\section\{'
    print("<h2>", end='')
    t.lexer.push_state('section')

def t_section_exit(t):
    r'\}'
    print("</h2>", end='')
    t.lexer.pop_state()

def t_SUBSECTION(t):
    r'\\subsection\{'
    print("<h3>", end='')
    t.lexer.push_state('subsection')

def t_subsection_exit(t):
    r'\}'
    print("</h3>", end='')
    t.lexer.pop_state()

def t_SUBSUBSECTION(t):
    r'\\subsubsection\{'
    print("<h4>", end='')
    t.lexer.push_state('subsubsection')

def t_subsubsection_exit(t):
    r'\}'
    print("</h4>", end='')
    t.lexer.pop_state()

def t_ENUMERATE(t):
    r'\\begin\{enumerate\}'
    print("<ol>", end='')
    t.lexer.push_state('enumerate')

def t_enumerate_ITEM(t):
    r'\\item'
    print(f"<li>", end='')
    t.lexer.push_state('item')

def t_enumerate_exit(t):
    r'\\end\{enumerate\}'
    print("</ol>", end='')
    t.lexer.pop_state()

def t_ITEMIZE(t):
    r'\\begin\{itemize\}'
    print("<ul>", end='')
    t.lexer.push_state('itemize')

def t_itemize_ITEM(t):
    r'\\item'
    print(f"<li>", end='')
    t.lexer.push_state('item')

def t_itemize_exit(t):
    r'\\end\{itemize\}'
    print("</ul>", end='')
    t.lexer.pop_state()

def t_item_exit(t):
    r'(?=\\item |\\end\{itemize\}|\\end\{enumerate\})'
    t.lexer.pop_state()

def t_BOLD(t):
    r'\\textbf\{'
    print("<b>", end='')
    t.lexer.push_state('bold')

def t_bold_exit(t):
    r'\}'
    print("</b>", end='')
    t.lexer.pop_state()

def t_ITALICS(t):
    r'\\textit\{'
    print("<i>", end='')
    t.lexer.push_state('italics')

def t_italics_exit(t):
    r'\}'
    print("</i>", end='')
    t.lexer.pop_state()

def t_UNDERLINE(t):
    r'\\underline\{'
    print("<u>", end='')
    t.lexer.push_state('underline')

def t_underline_exit(t):
    r'\}'
    print("</u>", end='')
    t.lexer.pop_state()

def t_TEXT(t):
    r'.|\n'
    print(t.value, end='')

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

with open("example.tex") as f:
    lexer.input(f.read())
    for tok in lexer:
        pass