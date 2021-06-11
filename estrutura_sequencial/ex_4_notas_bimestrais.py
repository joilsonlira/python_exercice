#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#--Variaveis--
primeira_nota = 0
segunda_nota = 0
terceira_nota = 0
quarta_nota = 0
media = 0.0

#--Solicitando notas-- todos os valores precisam ser convertidos para INT porque a função "input" transforma em STR.
primeira_nota = int(input("Me informe a primeira nota: "))
segunda_nota = int(input("Me informe a segunda nota: "))
terceira_nota = int(input("Me informe a terceira nota: "))
quarta_nota = int(input("Me informe a quarta nota: "))

#--Calculando media--
media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

#--Mostrando media--
print("A media é", media)