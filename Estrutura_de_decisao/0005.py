'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 Amensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez'''

nota1 = nota1 = float(input("Insira a nota 1 entre 0 e 10 \n"))
while nota1 <0 or nota1 > 10:
    nota1 = float(input("Insira a nota 1 entre 0 e 10 \n"))

nota2 = nota2 = float(input("Insira a nota 2 entre 0 e 10 \n"))
while nota2 <0 or nota2 > 10:
    nota2 = float(input("Insira a nota 2 entre 0 e 10 \n"))

media = (nota1 + nota2) / 2

if media < 7:
    print("Reprovado")
elif media < 10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
