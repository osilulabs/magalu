'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

Salario = float(input("Digite o seu salário: \n"))
if Salario <= 280:
    print("Salario atual: R$", round(Salario), "\nPercentual de aumento 20%\nValor do aumento R$:", round(Salario)*0.2, "\nSeu novo salário será de: R$", round(Salario)*1.2)
elif Salario > 280 and Salario <= 700:
    print("Salario atual: R$", round(Salario), "\nPercentual de aumento 15%\nValor do aumento R$:", round(Salario)*0.15, "\nSeu novo salário será de: R$", round(Salario)*1.15)
elif Salario > 700 and Salario <= 1500:
    print("Salario atual: R$", round(Salario), "\nPercentual de aumento 10%\nValor do aumento R$:", round(Salario)*0.1, "\nSeu novo salário será de: R$", round(Salario)*1.1)
else:
     print("Salario atual: R$", round(Salario), "\nPercentual de aumento 5%\nValor do aumento R$:", round(Salario)*0.05, "\nSeu novo salário será de: R$", round(Salario)*1.05)

