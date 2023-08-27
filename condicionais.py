# Traduza as afirmações a seguir para condicionais em Python:
# Se idade é maior que 60, escreva: "Você tem direito aos benefícios":
idade = int(input("Qual a sua idade? "))

if idade > 60:
    print("Você tem direito aos beneficios")

# Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto!":
dano = int(input("Qual o valor do dano? "))
escudo = int(input("Qual o valor do escudo? "))

if dano > 10 and escudo == 0:
    print("Você está morto!")

# Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"
norte = True
sul = False
leste = True
oeste = False

if norte or sul or leste or oeste == True:
    print("Você escapou!")


# Condicionais Compostas
# Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não é um ano bissexto".
ano = int(input("Digite o ano: "))
if ano % 4 == 0:
    print("Pode ser um ano bissexto.")
else:
    print("Definitivamente não é um ano bissexto")

# Se ambas as variáveis booleanas cima e baixo forem True, escreva: "Decida-se!", caso contrário, escreva: "Você escolheu um caminho!"
cima = False
baixo = True

if cima and baixo == True:
    print("Decida-se!")
else:
    print("Você escolheu um caminho!")
