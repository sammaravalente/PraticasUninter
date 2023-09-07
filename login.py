# Escreva um algoritmo que realize um login em um sistema.
# O usuário deve informar seu nome e senha.

login = input("Digite seu nome: ")
while login != "Python":
    print("Você digitou o nome incorreto. Tente novamente.")
    login = input("Digite seu nome: ")
    continue

senha = input("Digite sua senha: ")
while senha != "python123":
    print("Você digitou a senha incorreta. Tente novamente.")
    senha = input("Digite sua senha: ")
    continue

print("Acesso concedido")


# ------------
# forma mais rápida

while True:
    nome = input("Qual o seu nome? ")
    if nome != "Python":
        continue
    senha = input("Qual a sua senha? ")
    if senha == "python123":
        break
print("Acesso concedido.")