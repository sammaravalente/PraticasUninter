# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

kmPercorridos = int(input('Qual a quantidade de KM percorridos pelo carro alugado? '))
diasAluguel = int(input('Por quantos dias o carro foi alugado? '))

precoKm = kmPercorridos * 0.15
precoCarro = diasAluguel * 60

total = precoKm + precoCarro

print(f'O carro alugado por {diasAluguel} dias custou R${precoCarro:.2f}. Foram {kmPercorridos}km percorridos que custaram R${precoKm:.2f}.')
print(f'O total a pagar é de R${total:.2f}.')