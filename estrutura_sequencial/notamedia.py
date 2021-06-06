#Faça um programa que peça as 4 notas bismestrais e mostre a média.

#Variaveis.
primeira_nota = 0
segunda_nora = 0
terceira_nora = 0
quarta_nota = 0
media = 0

#solicitando notas ao usuario.
primeira_nota = int(input("Primeira nota: "))
segunda_nota = int(input("Segunda nota: "))
terceira_nota = int(input("Terceira nota: "))
quarta_nota = int(input("Quarta nota: "))

#Calculo de media.
media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

#Exibindo media.
print("Média: ", media)
