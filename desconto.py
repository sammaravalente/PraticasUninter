# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto

# fórmula de desconto: valor do desconto = preço original x (porcentagem de desconto / 100%)

precoProduto = float(input('Qual o valor do produto? '))
desconto = float(input('Qual o percentual de desconto? '))
calcDesconto = precoProduto * (desconto/100)
precoFinal = precoProduto - calcDesconto

print(f'O preço original do produto é de R${precoProduto:.2f}')
print(f'O desconto é de {desconto:.0f}%. Com desconto aplicado, o preço final do produto é de R${precoFinal:.2f}')