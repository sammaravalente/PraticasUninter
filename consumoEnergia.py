# Escreva um programa que calcula o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.

# Preço por tipo e faixa de consumo:
    # Residencial
        # até 500kWh - R$0,40
        # acima de 500kWh - R$0,65
    # Comercial
        # até 100kWh - R$0,55
        # acima de 1000kWh - R$0,60
    # Industrial
        # até 5000kWh - R$0,55
        # acima de 5000kWh - R$0,60


qtdKwh = float(input("Qual a quantidade de KWh consumida? "))
print("Tipos de instalação:")
print("R - Residencial")
print("C - Comercial")
print("I - Industrial")
inst = input("Qual o tipo de instalação? ")

if inst == "R":
    if qtdKwh <= 500:
        print(f"Total a pagar: R${qtdKwh * 0.40:.2f}")
    else:
        print(f"Total a pagar: R${qtdKwh * 0.65:.2f}")
elif inst == "C":
    if qtdKwh <= 100:
        print(f"Total a pagar: R${qtdKwh * 0.55:.2f}")
    else:
        print(f"Total a pagar: R${qtdKwh * 0.60:.2f}")
elif inst == "I":
    if qtdKwh <= 5000:
        print(f"Total a pagar: R${qtdKwh * 0.55:.2f}")
    else:
        print(f"Total a pagar: R${qtdKwh * 0.60:.2f}")
else:
    print("Instalação Inválida.")