""" aula 5: 2021-03-23

Somador on/off
    -semáforo está on de início
    -lê do input
    -reagit a estímulos
       r'[oO][nN]' --> ligar o semáforo
       r'(o|O)(f|F){2}' --> desligar o semáforo
       r'\d+' --> Se semáforo ligado --> soma = soma + valor('\d+')
       r'=' --> Escrever a soma no output

"""

import sys
import re

semaforo = True
soma = 0

for linha in sys.stdin:
    if re.search(r'[oO][nN]', linha):
        semaforo = True
    elif re.search(r'(o|O)(f|F){2}', linha):
        semaforo = False
    elif m := re.search(r'(\d+)', linha):
        if semaforo:
            soma += int(m.group(1))
    elif re.search(r'=', linha):
        print(soma)

# for linha in sys.stdin:
#     if results := re.findall(r'([oO][nN])|([oO][fF]{2})|(\d+)|(=)', linha):
#         for (on, off, dig, pr) in results:
#             if on:
#                 semaforo = True
#             elif off:
#                 semaforo = False
#             elif dig:
#                 if semaforo:
#                     soma += int(dig)
#             elif pr:
#                 print(soma)
