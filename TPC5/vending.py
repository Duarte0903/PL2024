import json
import re
import ply.lex as lex

tokens = [
        'LISTAR',
        'SAIR',
        'SALDO',
        'MOEDA',
        'SELECIONAR',
        'ADICIONAR'
    ]

def t_ADICIONAR(t):
    r'ADICIONAR\s\w+\s\d+'
    produto = t.value.split()[1]
    quantidade = int(t.value.split()[2])
    if produto in t.lexer.data['stock']:
        if produto['id'] == produto:
            produto['quantidade'] += quantidade
            produto['preco'] = preco
            with open("vending.json", "w", encoding="utf-8") as file:
                json.dump(t.lexer.data, file, indent=2, ensure_ascii=False)
            print(f"Produto reposto com sucesso: {produto}")
        else:
            print(f"Produto inexistente: {produto}")
    else:
        print("Adicionar novo produto: " + produto)
        id_produto = t.lexer.data['stock'][-1]['id'] + 1
        preco = input("Insira o preço do produto: ")
        with open("vending.json", "w", encoding="utf-8") as file:
            t.lexer.data['stock'].append({'id': id_produto, 'nome': produto, 'quantidade': quantidade, 'preco': preco})
            json.dump(t.lexer.data, file, indent=2, ensure_ascii=False)
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s\d+'
    produto_id = int(t.value.split()[1])
    for elem in t.lexer.data['stock']:
        if elem['id'] == produto_id:
            if elem['quantidade'] > 0:
                print(f"Produto selecionado: {elem['nome']}")
                elem['quantidade'] -= 1
                with open("vending.json", "w", encoding="utf-8") as file:
                    json.dump(t.lexer.data, file, indent=2, ensure_ascii=False)
            else:
                print(f"Produto esgotado: {elem['nome']}")
            break
    else:
        print(f"Produto inexistente: {produto_id}")
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
    print("""maq:
cod | nome | quantidade |  preço
------------------------------------""")
    for produto in t.lexer.data['stock']:
        print(f"{produto['id']} | {produto['nome']} | {produto['quantidade']} | Preço: {produto['preco']}\n")
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
        - SELECIONAR <ID produto>  
        - ADICIONAR <Nome produto> <quantidade>
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