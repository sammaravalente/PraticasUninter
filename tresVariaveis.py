# Crie três variáveis distintas. Uma contendo o nome da sua comida favorita. Outra contendo o seu ano de nascimento, e a terceira contendo o resultado da divisão do seu ano de nascimento pela sua idade. Armazene em uma quarta variável do tipo string uma mensagem que contenha todas as informações das variáveis acima. Resolva o exercício da maneira clássica de composição e também da maneira mais moderna.

# Maneira clássica de composição

comidaFav = 'Pizza Portuguesa'
anoNascimento = 2000
divisao = anoNascimento / 22
msg = 'Ela nasceu nos anos %d, gosta de %s. O seu ano de nascimento dividido pela sua idade dá %.2f.' % (anoNascimento, comidaFav, divisao)
print(msg)


# Maneira moderna

comidaFav = 'Pizza Portuguesa'
anoNascimento = 2000
divisao = anoNascimento / 22
msg = 'Ela nasceu nos anos {}, gosta de {}. O seu ano de nascimento dividido pela sua idade dá {:.2f}.' .format(anoNascimento, comidaFav, divisao)
print(msg)

## ou

comidaFav = 'Pizza Portuguesa'
anoNascimento = 2000
divisao = anoNascimento / 22
msg = f'Ela nasceu nos anos {anoNascimento}, gosta de {comidaFav}. O seu ano de nascimento dividido pela sua idade dá {divisao:.2f}.'
print(msg)