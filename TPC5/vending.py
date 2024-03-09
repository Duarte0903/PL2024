import json
import re
import ply.lex as lex

tokens = [
        'LISTAR',
        'SAIR',
        'SALDO',
        'MOEDA',
        'SELECIONAR',
    ]

def t_SELECIONAR(t):
    r'SELECIONAR\s\w+'
    produto = t.value.split()[1]
    if produto in t.lexer.data:
        if t.lexer.saldo >= t.lexer.data[produto]['preco']:
            t.lexer.saldo -= t.lexer.data[produto]['preco']
            print(f"Compra efetuada com sucesso: {produto}")
        else:
            print(f"Saldo insuficiente para comprar: {produto}")
    else:
        print(f"Produto inexistente: {produto}")
    return t

t_ignore = ' \t\n'

def t_SALDO(t):
    r'SALDO'
    print(f"Saldo disponivel: {t.lexer.saldo}€")
    return t

def t_MOEDA(t):
        r'MOEDA((\s(5|10|20|50)c)|\s(1|2)e)+'
        matches_digits = re.findall(r'\d{1,2}', t.value)  
        matches_e_c = re.findall(r'[ec]', t.value)      
        groups = list(zip(matches_digits, matches_e_c)) 
        for elem in groups:
            if elem[1] =='c':
                t.lexer.saldo+=int(elem[0]) / 100
            else:
                t.lexer.saldo+=float(elem[0])

        return t

def t_LISTAR(t):
    r'LISTAR'
    for produto, detalhes in t.lexer.data.items():
        print(f"{produto}: {detalhes['preco']}€")
        
    return t

def t_SAIR(t):
    r'SAIR'
    print(f"Troco: {t.lexer.saldo}€")
    t.lexer.flag=1
    return t

def t_error(t):
    t.lexer.skip(1)

def main():
    lexer = lex.lex()
    
    with open("vending.json", "r") as file:
        data = json.load(file)

    lexer.data = data
    lexer.flag = 0
    lexer.saldo = 0
    
    mensagem_inicial = """
        Bem-vindo à máquina de venda automática.
        Comandos disponíveis:
        - SALDO
        - MOEDA <quantia>e e/ou <quantia>c
        - LISTAR
        - SELECIONAR <produto>  
        - SAIR
        """
    
    print(mensagem_inicial)

    while lexer.flag == 0:
        input_user = input("Operação a realizar: ")
        lexer.input(input_user)
        token = lexer.token()
        if not token:
            print("Comando inválido")

if __name__ == "__main__":
    main()