# TPC5: Máquina de vending

## Autor: 

- Duarte Machado Leitão
- A100550

## Resumo

Este trabalho tem como objetivo a implementação de uma máquina de vending. Neste sentido, o programa deve responder às seguintes instruções:
- LISTAR: Lista todos os produtos da máquina, enumerando os seus ids, nomes e preços.
- MOEDA: Permite ao utilizador introudiz dinheiro (1e, 2e, 5c, 10c, 20c, 50c). Vária moedas podem ser introduzidas em sequência.
- SALDO: Diz ao utilizador o seu saldo atual.
- SELECIONAR: Permite comprar produtos, introduzindo o seu id.
- SAIR: Dá ao utilizador o seu troco e sai do programa.

## Resolução

A lista tokens define os tipos de tokens que o analisador léxico reconhecerá. Cada token é definido por uma função com um prefixo t_. Essas funções usam expressões regulares para corresponder a entrada do usuário a um tipo de token específico.

A função t_ADICIONAR é chamada quando o usuário quer adicionar um produto à máquina. Ela verifica se o produto já existe no estoque. Se existir, a quantidade é aumentada. Se não, um novo produto é criado.

A função t_SELECIONAR é usada para selecionar um produto para compra. Ela verifica se o produto existe e se há quantidade suficiente disponível. Se sim, a quantidade do produto é reduzida.

A função t_SALDO exibe o saldo atual do usuário.

A função t_MOEDA é usada para adicionar dinheiro à máquina. Ela aceita valores em euros e centimos.

A função t_LISTAR lista todos os produtos disponíveis na máquina.

A função t_SAIR é usada para terminar a sessão do usuário e devolver o troco.

A função t_error é chamada quando a entrada do usuário não corresponde a nenhum dos tokens definidos.