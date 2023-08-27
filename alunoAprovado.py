# Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando.
# Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno em cada matéria e informe, na tela, se ele passou de ano ou não.

mat1 = float(input("Nota da matéria 1: "))
mat2 = float(input("Nota da matéria 2: "))
mat3 = float(input("Nota da matéria 3: "))

if mat1 >= 7 and mat2 >= 7 and mat3 >= 7:
    print("Você passou de ano")
else:
    print("Você não passou de ano")
