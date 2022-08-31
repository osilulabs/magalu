'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
num_int_1 = int(input("Insira um numero inteiro"))
num_int_2 = int(input("Insira outro numero inteiro"))
num_real = float(input("Insira outro numero real"))
print("(2 x", num_int_1,") + (",num_int_2, "/2)=", (num_int_1*2)+(num_int_2/2))
print("(3 x", num_int_1, ") + (", num_real, ")=", float(num_int_1 * 3)+num_real)
print(num_real, " elevado ao cubo é = ",num_real**3)