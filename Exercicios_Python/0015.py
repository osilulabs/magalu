'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''
valor_hora = float(input("Entre com a valor do teu salário por hora: \n"))
qtd_hora_mes = int(input("Entre com a quantidade de horas trabalhadas: \n"))

salario_bruto = valor_hora * qtd_hora_mes
IR = salario_bruto*0.11
INSS = salario_bruto*0.08
contri_sind = salario_bruto*0.05
Tot_descontos = IR+INSS+contri_sind
sal_liquido = salario_bruto - Tot_descontos

print("Valor Bruto no Mês: ",salario_bruto)
print("Desconto Imposto de Renda: R$", IR)
print("Desconto INSS: R$", INSS)
print("Desconto Sindical: R$", contri_sind)
print("Total de descontos: R$", Tot_descontos)
print("Pagamento líquido : R$", sal_liquido)
