'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

from re import A


nota1 = float(input("Insira a primeira nota: \n"))
while nota1 <0 or nota1 > 10:
    nota1 = float(input("Por gentileza, inserir valor entre 0 e 10 \n"))

nota2 = nota2 = float(input("Insira a segunda nota \n"))
while nota2 <0 or nota2 > 10:
    nota2 = float(input("Por gentileza, inserir valor entre 0 e 10 \n"))

media = (nota1 + nota2) / 2

if  media > 9 and media <= 10:
        conceito = 'A'
        situacao = "Aprovado"

elif media > 7.5 and media <= 9:
        conceito = 'B'
        situacao = "Aprovado"

elif media > 6 and media <= 7.5:
        conceito = 'C'
        situacao = "Aprovado"

elif media > 4 and media <= 6:
        conceito = 'D'
        situacao = "Reprovado"

else:
    conceito = 'E'
    situacao = "Reprovado"

print("primeira nota ", nota1)
print("segunda nota", nota2)
print("Sua média é ", media)
print("Seu conceito foi: ",conceito,". Você está:",situacao,"!")

