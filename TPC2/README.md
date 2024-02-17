# TPC2: Markdown 2 HTML

## Autor

- Duarte Machado Leitão
- A100550

## Resumo

O objetivo é implementar parte de um conversor de markdown para HTML. O mesmo deverá ser capaz de realizar as seguintes tarefas:

- **Converter cabeçalhos**
    ```
    in: # texto ou ## texto ou ### texto
    out: <h1>texto</h1> ou <h2>texto</h2> ou <h3>texto</h3>
    ```

- **Converter os elementos bold**
    ```
    in: **bold** ou __bold__
    out: <b>bold</b>
    ```

- **Converter os elementos itálicos**
    ```
    in: *italico*
    out: <i>italico</i>
    ```

- **Converter listas numeradas**
    ```
    in: 
        1. Primeiro item
        2. Segundo item
        3. Terceiro item

    out:
        <ol>
            <li>Primeiro item</li>
            <li>Segundo item</li>
            <li>Terceiro item</li>
        </ol> 
    ```

- **Converter os links**
    ```
    in: [página da UC](http://www.uc.pt)
    out: <a href="http://www.uc.pt">página da UC</a>
    ```

- **Converter imagens**
    ```
    in: ![Coelho](https://i.imgur.com/0HmvAdB.jpeg)
    out: <img src="https://i.imgur.com/0HmvAdB.jpeg" alt="Coelho">
    ```

## Resolução

O conversor começa por ler o ficheiro markdown introduzido nos argumentos. De seguida é criado um ficheiro html com o mesmo nome para escrever os resultados. Com o ficheiro criado, é invocado o conversor que usa expressões regulares para substituir sintaxe markdown por sintaxe html. No final, o conversor invoca uma função que adiciona à conversão os elementos necessários para completar a página html que será escrita no ficheiro de output criado no início do programa.