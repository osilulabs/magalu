'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

altura = float(input("Insira sua altura: "))
genero = input("Qual seu genero? \nF para feminino \nM para Masculino \n")

if(genero == 'M' or genero == 'm'):
    peso_ideal = (72.7*altura) - 58

elif(genero == 'F' or genero == 'f'):
    peso_ideal = (62.1*altura) - 44.7


else: print("Entre com valores válidos")

print("Seu peso ideal é :", round(peso_ideal), "kg")
