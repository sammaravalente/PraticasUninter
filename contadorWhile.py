# Escreva um algoritmo que imprima na tela somente valores em um intervalo especificado pelo usuário e que sejam números pares

inicio = int(input("Qual valor deseja iniciar a contagem? "))
fim = int(input("Qual valor deseja encerrar a contagem? "))

x = inicio
while x <= fim:
    if (x % 2 == 0):
        print(x)
    x = x + 1