'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

horas_mes = float(input("Digite a quantidade de horas trabalhadas: \n"))
salario_hora = float(input("Digite seu salário por hora: \n"))

Salario = salario_hora * horas_mes
desc_ir_ate_900 = 0
desc_ir_901_1500 = Salario*0.05
desc_ir_1501_2500 = Salario*0.1
desc_ir_maior_2500 = Salario*0.2
inss = Salario * 0.10
fgts = Salario*0.11

if Salario <= 900:
    print("(+) Salario Bruto: R$ (", salario_hora, horas_mes, ") R$", round(Salario))
    print("(-) IR: R$ ",round(desc_ir_ate_900 ))
    print("(-) INSS R$: ", round(inss))
    print("FGTS: R$ ", round(fgts))
    print("Total de descontos: R$ ", desc_ir_ate_900+inss)
    print("Salário líquido: R$ ", Salario - (desc_ir_ate_900+inss))

elif Salario <= 1500 :
    print("(+) Salario Bruto: R$ (", salario_hora, horas_mes, ") R$", round(Salario))
    print("(-) IR: R$ ",round(desc_ir_901_1500 ))
    print("(-) INSS R$: ", round(inss))
    print("FGTS: R$ ", round(fgts))
    print("Total de descontos: R$ ", desc_ir_901_1500+inss)
    print("Salário líquido: R$ ", Salario - (desc_ir_901_1500+inss))

elif Salario <= 2500 :
    print("(+) Salario Bruto: R$ (", salario_hora, horas_mes, ") R$", round(Salario))
    print("(-) IR: R$ ",round(desc_ir_1501_2500 ))
    print("(-) INSS R$: ", round(inss))
    print("FGTS: R$ ", round(fgts))
    print("Total de descontos: R$ ", desc_ir_1501_2500+inss)
    print("Salário líquido: R$ ", Salario - (desc_ir_1501_2500+inss))

else:
    print("(+) Salario Bruto: R$ (", salario_hora, horas_mes, ") R$", round(Salario))
    print("(-) IR: R$ ",round(desc_ir_maior_2500 ))
    print("(-) INSS R$: ", round(inss))
    print("FGTS: R$ ", round(fgts))
    print("Total de descontos: R$ ", desc_ir_maior_2500+inss)
    print("Salário líquido: R$ ", Salario - (desc_ir_maior_2500+inss))
