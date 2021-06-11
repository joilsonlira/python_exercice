#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

#--variaveis--
lado_y = float
lado_x = float
area = float
dobro = float

#--solicitando lados X e Y--
lado_y = float(input("Informe o lado y:"))
lado_x = float(input("Informe o lado x:"))

#--calculando area e o dobro da area--
area = lado_x * lado_y
dobro = area * 2 #-- dobro da área.--

print("A áres do quadrado é", area, ", o dobro da área é", dobro)
