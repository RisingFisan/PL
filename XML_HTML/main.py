import re

def xml2html(rel):
    encoding = re.search(r'<\?xml(?:.*?)encoding=(\"(.*?)\")(?:.*?)\?>', rel).group(1)

    relatorio = re.sub(r'<\?xml(?:.*)\?>', r'<!DOCTYPE html>\n', rel)

    relatorio = re.sub(
        r'<relatorio>((?:.|\n)*?)</relatorio>',
rf'''<html>
    <head>
        <meta charset={encoding}/>
        <title>relatorio</title>
    </head>
    <body>
        \1
    </body>
</html>
''',
     relatorio)

    relatorio = re.sub(
        r'<titulo>((?:.|\n)*)</titulo>',
        r'<h1>\1</h1>',
        relatorio
    )

    relatorio = re.sub(
        r'<autores>((?:.|\n)*)</autores>',
        r'<h3>Autores</h3>\n<ul>\1</ul>',
        relatorio
    )

    print(relatorio)

with open("relatorio.xml") as f:
    content = f.read()
    xml2html(content)