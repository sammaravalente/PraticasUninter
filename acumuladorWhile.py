# Escreva um algoritmo que calcule a sua média de notas em determinada disciplina.

# Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas.

soma = 0
cont = 1

while cont <= 5:
    nota = float(input(f"Nota da disciplina {cont}: "))
    soma = soma + nota # ou soma = soma += nota (operador especial de atribuição)
    cont = cont + 1 # cont = cont += 1
media = soma / 5
print(f"Média final do aluno: {media}")