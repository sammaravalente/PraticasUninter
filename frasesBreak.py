# Escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuário. Encerre o algoritmo quando a palavra 'sair' for digitada.

frase = input("Digite uma frase ou palavra ou 'sair' para encerrar o programa: ")

while frase != "sair":
    frase = input("Digite uma frase ou palavra: ")
    if frase == "sair":
        print("Você saiu do programa com sucesso.")
        break