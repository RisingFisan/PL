import re

detect = re.compile(r"(?:\w+\.)*\w+@(?:\w+\.)+\w+")
emails = set()

with open("dataset.txt", encoding='utf-8') as f:
    N = int(f.readline())
    for i in range(N):
        line = f.readline().strip()
        if ms := detect.findall(line):
            for m in ms: emails.add(m)

print(';'.join(sorted(emails)))