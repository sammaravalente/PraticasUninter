# Realize a sequência de print com for e while:
# a) Inteiros de 3 até 12, com 12 incluso

for i in range (3, 13):
    print(i)

i = 3
while i <= 12:
    print(i)
    i += 1

# b) Inteiros de 0 até 9, excluindo 9, com passo de 2

for i in range (0, 9, 2):
    print(i)

i = 0
while i < 9:
    print(i)
    i += 2