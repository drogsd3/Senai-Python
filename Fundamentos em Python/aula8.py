#REVISÃO
idade = int(input("Digite sua idade: "))
if idade > 17:
    print("Você é maior de idade!")
else:
    print("Você não é maior de idade!")

media = float(input("\nDigite a media do aluno: "))

if media > 8:
    print("Muito bom")
elif media >= 6:
    print("Bom")
else:
    print("Ruim")

numero = int(input("\nDigite um numero: "))
if numero > 0:
    print("Positivo!")
elif numero < 0:
    print("Negativo!")
else:
    print("Neutro!")