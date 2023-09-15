# Escreva uma rotina que crie uma borda ao redor de uma palavra para destacá-la como sendo um título. A rotina deve receber como parâmetro a palavra a ser destacada. O tamanho da caixa de texto deverá ser adaptável conforme o tamanho da palavra.



def borda():
    nome = input("Digite seu nome: ")
    print("*", "-" * len(nome), "*")
    print("|",  nome, "|")
    print("*", "-" * len(nome), "*")

borda()