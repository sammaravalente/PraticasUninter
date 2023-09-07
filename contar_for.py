# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos). Implemente o lanço usando *for*.

soma = 0 # somar todos os valores pares
cont = 0 # qtd de vezes que o número é par
for i in range (1, 101):
    if i % 2 == 0:
        soma += i
        cont += 1
media = soma // cont
print(media)
