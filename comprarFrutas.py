# Escreva um algoritmo em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções: 1 - maçã, 2 - laranja e 3 - banana

# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.

# Considere que uma maçã custa R$2,30, uma laranja R$3,60 e uma banana, R$1,85


print("Barraca de Frutas!")
print("1 - Maçã")
print("2 - Laranja")
print("3 - Banana")
fruta = int(input("Escolha a sua opção de compra: "))
unidades = int(input("Quantas unidades? "))

if fruta == 1:
    print(f"Você comprou {unidades} unidades de Maçã por R${unidades * 2.30:.2f}.")
elif fruta == 2:
    print(f"Você comprou {unidades} unidades de Laranja por R${unidades * 3.60:.2f}.")
elif fruta == 3:
    print(f"Você comprou {unidades} unidades de Banana por R${unidades * 1.85:.2f}.")
else:
    print("Produto inexistente.")


