'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''


vogal = ('A','E','I','O','U')
letra = input("Digite uma letra: \n").upper()

if letra in vogal:
    print("A letra (", letra, ") é uma vogal")
elif letra.isalpha():
    print("A letra (", letra, ") é uma consoante")
else:
    print("(", letra, ") não é uma letra")

