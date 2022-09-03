'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''


dados = {1: "Domingo" ,  2: "Segunda", 3: "Terça", 4: "Quarta", 5:"Quinta", 6:"Sexta", 7:"Sábado"}
dia_semana = int(input("Digite o dia da semana sendo:\n(1) Domingo \n(2) Segunda\n(3) terça \n(4) Quarta \n(5) Quinta \n(6) Sexta \n(7) Sábado \n"))

while dia_semana not in (dados):
    dia_semana = int(input("Valor inválido! Favor inserir dados conforme menu:\n(1) Domingo \n(2) Segunda\n(3) terça \n(4) Quarta \n(5) Quinta \n(6) Sexta \n(7) Sábado \n"))

print(dados[dia_semana])

    
