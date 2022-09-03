'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = turno = input("Qual seu turno?\nM - Matutino \nV - Vespertino \nN - Noturno\n: ").upper()

while turno not in ('V'  'M'  'N'):
    turno = input("Qual seu turno?\nM - Matutino \nV - Vespertino \nN - Noturno\n: ").upper()

if turno == 'M': 
    print("Bom dia")
elif turno == 'V': 
    print("Boa tarde")
else:
    print("Boa noite")

