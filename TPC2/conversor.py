import sys
import re

def construir_pagina_html(html):
    pagina = f'''
<!DOCTYPE html>\n
<html>\n
<head>\n
<title>Conversor</title>\n
</head>\n
<body>\n
{html}
</body>\n
</html>
    '''
    return pagina

def md_to_html(md):    
    # titulos
    md = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md, flags=re.M)
    md = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md, flags=re.M)
    md = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md, flags=re.M)

    # bold
    md = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md)

    # itálico
    md = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md)

    # listas numeradas
    md = re.sub(r'(?<=\n)(\d+\.) (.+?)(?=\n\n|\n\s*\d+\.)', r'<li>\2</li>', md)
    md = re.sub(r'(\n<li>.+?</li>)+', r'\n<ol>\g<0>\n</ol>', md)

    # imagens
    md = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', md)

    # links
    md = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md)
    
    return construir_pagina_html(md)

def main(imp):
    if len(imp) == 2 and imp[1].endswith(".md"):
        # abrir markdown
        with open(imp[1], "r", encoding="utf-8") as file:
            md = file.read()

        # criar um html com o mesmo nome que o md
        with open(imp[1].replace(".md", ".html"), "w", encoding="utf-8") as html:
            html.write(md_to_html(md))

    else:
        print("Ficheiro md não foi introduzido")

if __name__ == "__main__":
    main(sys.argv)