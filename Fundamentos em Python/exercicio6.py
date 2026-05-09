#Usando input 
nota1 = float(input("Digite a 1° nota do aluno: "))
nota2 = float(input("Digite a 2° nota do aluno: "))
nota3 = float(input("Digite a 3° nota do aluno: "))
nota4 = float(input("Digite a 4° nota do aluno: "))

print("\nA 1° nota é: ", nota1)
print("A 2° nota é: ", nota2)
print("A 3° nota é: ", nota3)
print("A 4° nota é: ", nota4)

media = (nota4+nota1+nota2+nota3)/4
print("\nA media das notas é: {:4.2f}".format(media))