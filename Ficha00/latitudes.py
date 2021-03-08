import re

with open("latitudes.txt") as f:
    for line in f.readlines():
        m = re.fullmatch(r"\(([-+]?0*[0-8]?\d(?:\.\d*)?|[+-]?0*90(?:\.0*)?),\s([-+]?0*(?:0?[0-9]?\d|1[0-7]\d)(?:\.\d*)?|[+-]?0*180(?:\.0*)?)\)",line.strip())
        if m:
            print(f"{m.string} - endereço válido\nLatitude: {m.group(1)}\nLongitude: {m.group(2)}\n")
        else:
            print(f"{line.strip()} - endereço inválido\n")