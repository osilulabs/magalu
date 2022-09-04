'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

lado_a = float(input("Insira o lado 1 do triângulo: "))
lado_b = float(input("Insira o lado 2 do triângulo: "))
lado_c = float(input("Insira o lado 3 do triângulo: "))

if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_c + lado_a > lado_b:
    if lado_a == lado_b and lado_a == lado_c:
        tipotriangulo = 'Equilatero'

    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        tipotriangulo = "Isósceles"

    else:
        tipotriangulo = "Escaleno"

    print("As medidas são de um triângulo ", tipotriangulo, ".")
else:
    print("Não forma um triangulo")
