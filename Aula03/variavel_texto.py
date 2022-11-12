from os import system #importa as bibliotecas do sistema operacional
system('cls')
# criação de variavel texto
# As variaves devem seguir um padrão
# snake_case, PascalCase ou camelCase
# nome_completo
# NomeCompleto
# nomeCompleto
nome_completo = 'Laercio Azevedo de Sá'
print(len(nome_completo)) # len = conta a quantidade de caracteres
print(nome_completo.count('e')) # conta a repetição de um caracter
print(nome_completo.upper())
print(nome_completo.lower())
print(nome_completo.capitalize())
print(nome_completo.find(' '))
espaco = nome_completo.find(' ')
nome = nome_completo[0:espaco]
print(nome)
print(nome_completo.replace(' ', '#'))
print(nome_completo.center(80,"*"))
print(nome_completo.split(' '))












