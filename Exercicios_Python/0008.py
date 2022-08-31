'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
hrs_trabalhadas = int(input("Quantas horas inteiras você trabalhou nesse mês? "))
salario_hr = float(input("Quanto você ganha por hora trabalhada? "))
Saldo = hrs_trabalhadas * salario_hr
print("O seu salário no mês será de R$",Saldo)

