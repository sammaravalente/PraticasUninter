# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
    # Equilátero (três lados iguais)
    # Isósceles (dois lados iguais)
    # Escaleno (três lados diferentes)

# Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois.

lado1 = int(input("Lado 1 do triângulo: "))
lado2 = int(input("Lado 2 do triângulo: "))
lado3 = int(input("Lado 3 do triângulo: "))

if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
    if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print("O triângulo é Escaleno.")
        elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
            print("O triângulo é Equilátero.")
        else:
            print("O triângulo é Isósceles.")
    else:
        print("Você não formou um triângulo. Tente novamente.")
else:
    print("Você não formou um triângulo. Tente novamente.")