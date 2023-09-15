# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo, e falso, caso contrário

def validar_string(string, min, max):


def validarString(s1, min, max):
    s1 = input("Digite uma frase ou palavra: ")
    min = int(input("Digite um número: "))
    max = int(input("Digite um número maior que o anterior digitado: "))
    if len(s1) >= min and len(s1) <= max:
        return True
    else:
        return False

validarString(s1, min, max)