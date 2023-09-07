# Crie um algoritmo que receba um valor do tipo inteiro via teclado. No entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos. Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado.

val = int(input("Digite um valor inteiro: "))

while val <= 0:
    print("O valor deve ser inteiro. Tente novamente.")
    val = int(input("Digite um valor: "))
    if val > 0:
        print(f"Valor digitado: {val}")