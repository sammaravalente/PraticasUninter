# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição, subtração, multiplicação ou divisão. Exiba na tela o resultado da operação desejada.

print("Calculadora:")
print("+ Adição")
print("- Subtração")
print("* Multiplicação")
print("/ Divisão")

operacao = input("Qual operação você deseja realizar? ")
if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
    valor1 = int(input("Digite o primeiro valor numérico: "))
    valor2 = int(input("Digite o segundo valor numérico: "))

if operacao == "+":  # adição
    print(valor1 + valor2)
elif operacao == "-":  # subtração
    print(valor1 - valor2)
elif operacao == "*":  # multiplicação
    print(valor1 * valor2)
elif operacao == "/":  # divisão
    print(valor1 // valor2)
else:
    print("A operação escolhida não existe. Encerrando...")
