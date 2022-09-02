''' Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''

import math

precoLata = 80.00
litros_lata = 18
precoGalao = 25.00
litros_galao = 3.6

metragem = float(input("Entre com a quantidade de metros quadrados a pintar:\n"))
litros_tinta = math.ceil(metragem / 6) * 1.1
if (litros_tinta % litros_lata >= 0 and litros_tinta % litros_lata <= (litros_galao * 6)):
    sobra_lata = (litros_tinta % litros_lata)
    latas_tinta = int(litros_tinta/18)
    print(latas_tinta)
    print(litros_tinta)
    print(sobra_lata)

'''custo = latas_tinta * preco
print("Você precisará de ", latas_tinta, "latas de tintas para pintar a área mencionada, e o custo será de R$", custo)'''
