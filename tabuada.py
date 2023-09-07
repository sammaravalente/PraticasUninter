# Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10 e, para cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10.

for i in range (1, 11):
    print(f"TABUADA DO {i}:")
    for j in range (1, 11):
        print(f"{i} * {j}:", i * j)
    continue