# TPC3: Somador on/off

## Autor

- Duarte Machado Leitão
- A100550

## Resumo

O objetivo é criar um programa python que some todas as sequências de dígitos que encontre num texto:

1. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado

2. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado

3. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída

## Resolução

O programa utiliza expressões regulares para identificar padrões específicos no input:

```python
    input_regex = r'(?P<soma>-?\d+)|(?P<ligar>[Oo][Nn])|(?P<desligar>[Oo][Ff]{2})|(?P<display>=)'
```

Existem quatro grupos de captura:

1. **soma:** -? O sinal de menos é opcional, permitindo que o número seja negativo. \d+ Corresponde a um ou mais dígitos (0-9).

2. **ligar:** Corresponde a todas as variações da palavra "on".

3. **desligar:** Corresponde a todas as variações da palavra "off".

4. **display:** Corresponde ao caractere '='.

Enquanto o input é processado no ciclo, são feitas correspondências entre o que é lido e os grupos de captura definidos no inicio. 