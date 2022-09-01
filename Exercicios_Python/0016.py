'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

import math

preco = 80.00
metragem = float(input("Entre com a quantidade de metros quadrados a pintar:\n"))
LT_Necessarios = math.ceil(metragem / 3)
latas_tinta = math.ceil(LT_Necessarios/18)
custo = latas_tinta * preco
print("Você precisará de ", latas_tinta, "latas de tintas para pintar a área mencionada, e o custo será de R$", custo)

