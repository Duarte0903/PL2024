# TPC6: Gramática Independente de Contexto

## Autor: 

- Duarte Machado Leitão
- A100550

## Resumo

Implementar uma Gramática Independente de Contexto (LL1) que permita tratar de prioridades de operações matemáticas, calculando os LA's (Look Aheads) dos diversos predicados.

Exemplos de operações:

```
    ?a
    b = a * 2/ (27-3)
    !a+b
    c = a*b / (a/b)
```

## Resolução

### Terminais

```
    T = {?, !, =, +, -, *, /, num, id_var, \n}
```

### Não-terminais

- Programa: P
- Declaração: D
- Expressão: E
- Termo: T
- Fator: F

### Produções

```
    p1: P -> D P | ε
    p2: D -> ? var | var = E
    p3: E -> E + T | E - T | T
    p4: T -> T * F | T / F | F
    p5: F -> ( E ) | num | var
```

### Lockahead Sets

```
    LA(P → D P): ?, var, !
    LA(P → ε): EOF (fim do arquivo)
    LA(D → ? var): ?
    LA(D → var = E): var
    LA(D → ! E): !
    LA(E → E + T): +, -, (, num, var
    LA(E → E - T): +, -, (, num, var
    LA(E → T): (, num, var
    LA(T → T * F): *, /, (, num, var
    LA(T → T / F): *, /, (, num, var
    LA(T → F): (, num, var
    LA(F → ( E )): (
    LA(F → num): num
    LA(F → var): var
```