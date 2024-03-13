import sys
import ply.lex as lex

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'INFO',
    'NUMBER',
    'FLOAT', 
    'EQUAL',
    'GREATER',
    'LESS',
    'COMMA',
)

t_SELECT = r'Select'
t_FROM = r'From'
t_WHERE = r'Where'

t_INFO = r'\w+'

t_NUMBER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_EQUAL = r'\='
t_GREATER = r'\>'
t_LESS = r'\<'
t_COMMA = r'\,'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def main(imp):
    with open(imp, 'r') as f:
        data = f.read()
        lexer = lex.lex()
        lexer.input(data)
        for token in lexer:
            print(token)

if __name__ == '__main__':
    main(sys.argv[1])