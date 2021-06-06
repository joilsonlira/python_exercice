"""
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a) o produto do dobro do primeiro com metade do segundo.
    b) a soma do triplo do primeiro com terceiro.
    c) o terceiro elevado ao cubo.
"""

#Variaveis
primeiro_inteiro = 0
segundo_inteiro = 0
numero_real = 0.0
resultado_primario = 0
resultado_secundario = 0

#Entrada dde valores.
primeiro_inteiro = int(input("Primeiro valor inteiro: "))
segundo_inteiro = int(input("Segundo valor inteiro: "))
numero_real = float(input("Valor real: "))

#Exercicio A.
resultado_primario = primeiro_inteiro *2
resultado_secundario = segundo_inteiro /2

#---Exibindo resposta
print("O dobro do primeiro valor inteiro é", resultado_primario, ". A metade do segundo valor inteiro é", resultado_secundario,".")

#Exercicio B.
resultado_primario = (primeiro_inteiro + numero_real) * 3

#---Exibindo resposta.
print("A soma do triplo do segundo valor inteiro com o valor real é", resultado_primario)

#Exercicio C.
resultado_primario = numero_real ** 3

#---Exibindo resultado.
print(resultado_primario)
