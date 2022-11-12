""" 
    Calcular area do retangulo
"""
from os import system
system("cls")
print("*** Calculo da area do retangulo ***\n\nInforme o primeiro lado:")
# print("Informe o primeiro lado: ")
lado1 = input()
print("Informe o segundo lado:")
lado2 = input()
# variavel.isnumeric = verifica se a variavel pode ser um número inteiro
# variavel.isdecimal = verifica se a variavel pode ser um número com casas decimais
print("O primeiro valor é numero inteiro?", lado1.isnumeric()) 
print("O segundo valor é numero inteiro?", lado2.isnumeric())
print("Será que vai dar certo ou vai dar erro?")
# int = transforma o valor da variavel em inteiro
# float = transforma o valor da variavel em float (decimal)
area = int(lado1) * int(lado2)
print("A area do retangulo é {} m² sendo os lados de {} x {}" . format(area, lado1, lado2))
print("A area do retangulo é", area, "m² sendo os lados de", lado1 , 'x', lado2)



