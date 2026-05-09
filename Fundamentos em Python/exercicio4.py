#Media nota
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunta nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1+nota2+nota3)/3
print("\nA media das notas é {:4.2f}".format(media))
if media >=6:
    print("Aprovado")
    print("Busque seu certificado na secretaria")
else:
    print("Reprovado")
print("O ano letivo acabou.")