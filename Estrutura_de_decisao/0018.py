'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
import sys

data = input("Entre com data: \n")

dia = int(data[:2])
mes = int(data[3:5])
ano = data[6:]
mes31 = {1, 3, 5, 7, 8, 10, 12}
mes30 = {4, 6, 9, 11}
mes29 = {}
mes28 = {}

if (ano.endswith("00") and int(ano) % 400 != 0) or (int(ano) % 4 != 0):
    mes28 = {2}
else:
    mes29 = {2}

if (data[2] != '/' or data[5] != '/') or (dia > 31 or dia == 0) or (mes > 12 or mes == 0) or (mes > 12 or mes == 0) or (dia > 30 and mes not in mes31) or (dia > 29 and (mes not in mes31 and mes not in mes30)) or (dia > 28 and (mes not in mes29 and mes not in mes31 and mes not in mes30)):
    print("Data inválida")

else:
    print("Esta data é válida" )

sys.exit(0)