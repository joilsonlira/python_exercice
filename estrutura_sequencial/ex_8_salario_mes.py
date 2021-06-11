"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

#--variaveis--
ganho_hora = float
hora_dia = int
dias_mes = 24
total_salario = int

#--perguntando ganho por hora e horas trabalhadas--
ganho_hora = float(input("Quanto ganha por hora?: "))
hora_dia = int(input("Quantas horas trabalha por dia?: "))

#--calculando salario por mês--
total_salario = (ganho_hora * hora_dia) * dias_mes

#--mostrando salario--
print("Salario total:",total_salario)