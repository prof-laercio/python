'''
    docstring é as 3 aspas = documentação do código
    programa para mostrar números inteiros em extenso
    somente numeros de 1 a 100
    array = use o simbolo de [ ] 
    tuple = use o simbolo de ( )
'''
from os import system
system('cls')
centenas = ("", "cento", "duzentos","trezentos")
dezenas = ("", "", "vinte", "trinta", "quarenta", 
    "cinquenta", "sessenta", 
    "setenta", "oitenta", "noventa")
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", 
    "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove")
valor = input('Informe um número de 1 a 99: ')
numerico = int(valor)
extenso = ''
if (numerico < 20):
    # print(numeros[numerico])
    extenso = numeros[numerico]
elif (numerico < 100):
    # print(valor[1:1])
    # print(dezenas[int(valor[0:1])], 'e', numeros[int(valor[1:2])])
    extenso = dezenas[int(valor[0:1])]
    if (valor[1:2]!="0"):
        extenso = f"{extenso} e {numeros[int(valor[1:2])]}"
print(extenso)
