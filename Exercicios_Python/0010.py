'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. Formula ((9 * c) / 5) + 32
'''
temp_C = float(input("Insira a temperatura em Celsius: "))
temp_F = ((9 * temp_C) / 5) + 32
print("A temperatura em Fahrenheit é: ", round(temp_F))
