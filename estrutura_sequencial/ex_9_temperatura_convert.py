"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9). 
"""

#--variaveis--
temperatura_f = float
temperatura_c = float

#--solicitando temperatura--
temperatura_f = float(input("Me informe a temperatura em Fahrenheit: "))

#--convertendo temperatura--
temperatura_c = 5 * ((temperatura_f - 32)/9)

#--mostrando temperatura convertida--
print("Temperatura em Celsius", temperatura_c)