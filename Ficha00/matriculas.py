import re

with open("matriculas.txt") as f:
    text = f.read()    

matches = re.findall(r"(\d{2}(?P<sep>-|:|\.\.\.)\d{2}(?:(?P=sep)\d{2}){2})", text)
print(f"{len(matches)} matrículas encontradas:\n" + '\n'.join(x[0] for x in matches))
