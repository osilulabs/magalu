'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

produto1 = float(input("Digite o preço do primeiro produto"))
produto2 = float(input("Digite o valor do segundo produto"))
produto3 = float(input("Digite o valor do terceiro produto"))
menor = min(produto1, produto2, produto3)
print("O menor valor é: ", min(produto1, produto2, produto3, sorted = (min())))

