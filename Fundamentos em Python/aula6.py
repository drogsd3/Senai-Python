#IF ELSE
numero = int(input("Digite um número: "))
if numero >=0:
    print("Esse número é positivo")
else:
    print("Esse número é negativo")

#Verificar idade
idade = int(input("\nDigite sua idade: "))
if idade >17:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#Verificar senha
senha = input("\nDigite a senha: ")
if senha == "python123":
    print("Acesso liberado")
else:
    print("Acesso negado")

#notas e media
nota1 = float(input("\nDigite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
nota3 = float(input("Digite a nota 3 do aluno: "))
nota4 = float(input("Digite a nota 4 do aluno: "))
media = (nota1+nota2+nota3+nota4)/4

if media >=6:
    print(f"O Aluno foi aprovado com a nota {media:4.2f}")
else:
    print(f"O Aluno não foi aprovado com a nota {media:4.2f}")