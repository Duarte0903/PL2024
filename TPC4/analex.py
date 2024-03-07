import sys
import re
from ply.lex import lex

tokens = (
    'COMMAND',
    'FROM',
    'WHERE',
    'VARS_TABS',
    'VALORES',
    'SIMBOLOS',
    'SEPARADORES'
)

t_COMMAND = r'[Ss][Ee][Ll][Ee][Cc][Tt]|[Uu][Pp][Dd][Aa][Tt][Ee]|[Dd][Ee][Ll][Ee][Tt][Ee]'
t_FROM = r'[Ww][Hh][Ee][Rr][Ee]'
t_WHERE = r'[Ff][Rr][Oo][Mm]'
t_VARS_TABS = r'[A-Za-z]\w*'
t_VALORES = r'-?\d+'
t_SEPARADORES = r",|;"
t_SIMBOLOS = r'>=|<=|<|>|==|='

t_ignore = ' \t'

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