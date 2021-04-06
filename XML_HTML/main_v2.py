import sys
import re

for line in sys.stdin:
    if res := re.search(r'<\?xml(.*)\?>', line):
        encoding = re.search(r'encoding=(\"(.*?)\")', res.group(1)).group(1)
        print(f"""<!DOCTYPE html>
        <head>
                <meta charset={encoding}/>
                <title>Relatório</title>
        </head>"""
    )

    elif res := re.search(r'<relatorio>', line):
        print("\t<body>")

    elif res := re.search(r'</relatorio>', line):
        print("\t</body>\n</html>")

    elif res := re.search(r'<titulo>(.*?)</titulo>', line):
        print(f"\t\t<h1>{res.group(1)}</h1>")

    elif res := re.search(r'<data>(.*?)</data>', line):
        print(f"\t\t<h2>{res.group(1)}</h2>")

    elif res := re.search(r'<autores>', line):
        print("\t\t<h3>Autores</h3>\n\t\t<ul>")

    elif res := re.search(r'<autor>', line):
        print("\t\t\t<li>")

    elif res := re.search(r'<nome>(.*?)</nome>', line):
        print(f"\t\t\t\t{res.group(1)}", end='')
    
    elif res := re.search(r'<numero>(.*?)</numero>', line):
        print(f" ({res.group(1)})", end='')

    elif res := re.search(r'<email>(.*?)</email>', line):
        print(f": {res.group(1)}")

    elif res := re.search(r'</autor>', line):
        print("\t\t\t</li>")

    elif res := re.search(r'</autores>', line):
        print("\t\t</ul>")

    elif res := re.search(r'<descricao>', line):
        print("\t\t<h3>Descrição</h3>")

    elif res := re.search(r'</descricao>', line):
        pass

    else:
        print(f"\t\t\t<p>{line.strip()}</p>")