#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#--variaveis--
raio = float
area = float

#--solicitando raio
raio = float(input("Me informe o raio:"))

#--calculando area
area = 3.14 * (raio**2)

#--mostra area
print("area do circulo:", area)
