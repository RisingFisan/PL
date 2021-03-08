import re

alinea_a = re.compile(r"(?i:alentejo)")
alinea_a_ans = set()

alinea_b_ans = dict()

alinea_c = re.compile(r"\.mp3")
alinea_c_ans = set()

alinea_d = re.compile(r"(?i:jesus)")
alinea_d_ans = set()

with open("Ficha01/arq-son.txt", encoding="utf-8") as f:
    for line in f.readlines():

        args = line.split('::')
        # alternativa com regex: args = re.split(r"::", line)

        # alínea a
        if alinea_a.match(args[0]):
            alinea_a_ans.add(args[2])

        # alínea b
        try:
            alinea_b_ans[args[0]] += 1
        except KeyError:
            alinea_b_ans[args[0]] = 1

        # alínea c
        if alinea_c.search(args[4]):
            alinea_c_ans.add(args[2])

        # alínea d
        if alinea_d.search(args[2]):
            alinea_d_ans.add(args[2])


print("Alínea a)\nAs músicas alentejanas são:", alinea_a_ans)
print("\n")
print("Alínea b)\nMúsicas por região:", alinea_b_ans)
print("\n")
print("Alínea c)\nAs músicas disponíveis em MP3 são:", alinea_c_ans)
print("\n")
print(f"Alínea d)\nExistem {len(alinea_d_ans)} músicas com 'Jesus' no título, que são:", alinea_d_ans)
