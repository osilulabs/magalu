'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
'''

ano = input("Insira um número")

if (ano.endswith("00") and int(ano) % 400 != 0) or (int(ano) % 4 != 0):
    print("O ano ", ano, "não é bissexto")

else:
    print("O ano ", ano, "é bissexto")