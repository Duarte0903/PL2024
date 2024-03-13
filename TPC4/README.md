# TPC3: Analisador lexico SQL

## Autor

- Duarte Machado Leitão
- A100550

## Resumo

O script deve separar o ficheiro em tokens baseados na linguagem SQL

Os resultados encontrados são escritos no terminal com a informação relativa a cada token sendo ele um número, uma variável, etc.

## Resolução

A variável tokens define todos os tipos de tokens que o analisador léxico reconhecerá. Cada token é representado por uma string.

As variáveis que começam com t_ são expressões regulares que definem como cada token é reconhecido. Por exemplo, t_SELECT é definido como a string 'Select', o que significa que o analisador léxico reconhecerá 'Select' como um token do tipo 'SELECT'.

A variável t_ignore define caracteres que o analisador léxico deve ignorar. Neste caso, espaços e tabulações serão ignorados.

A função t_newline(t) é uma função especial que lida com novas linhas, incrementando o número de linha do analisador léxico.

A função t_error(t) é chamada quando um caractere ilegal é encontrado. Ela imprime uma mensagem de erro e avança para o próximo caractere.