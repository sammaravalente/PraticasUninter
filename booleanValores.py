# Condicional Simples:

# Desenvolva um programa que lê dois valores numéricos inteiros e compara se o primeiro é maior do que o segundo, utilizando uma condicional simples.
# Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor digitado é maior do que o segundo.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if (num1 > num2):
    print(f"O número {num1} é maior que o número {num2}")


# Condicional Composta:

# Desenvolva um programa que lê um valor inteiro e descobre se ele é par ou ímpar.

num = int(input("Digite um número: "))

if (num % 2 == 0):
    print(f"O número {num} é PAR.")
else:
    print(f"O número {num} é ÍMPAR.")