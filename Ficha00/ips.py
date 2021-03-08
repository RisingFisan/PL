import re

with open("ips.txt") as f:
    for line in (x.strip() for x in f.readlines()):
        ipv4m = re.match(r"(([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(?:\.|$)){4}",line)
        if ipv4m:
            print(f"{ipv4m.string} é um endereço IPv4.")
        else:
            ipv6m = re.match(r"[0-9a-fA-F]{4}(?:\:[0-9a-fA-F]{4}){7}",line)
            if ipv6m:
                print(f"{ipv6m.string} é um endereço IPv6.")
            else:
                print(f"{line} não é um endereço válido.")
