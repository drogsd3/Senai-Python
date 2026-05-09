#imports
import datetime

#Variaveis
nome = "Douglas"
cidade = "Ibiúna"
idade = 27
comida = "pizza"
cor="Azul"
print("Meu nome é:", nome, "moro em", cidade, "e tenho", idade,"anos.")
print(f"Minha comida favorita é {comida}, já a minha cor favorita é {cor}.")

#Calculos
a = 5
b = 2
ano_nascimento = 1997
print("A multiplicação dos dois numeros fica:",a*b)
print("A soma dos numeros fica:",a+b)
print("A substração dos numeros fica:",a-b)
print("A divisão fracionaria fica:",a/b)
print("A divisão inteira fica:", a//b)
print("O modulo da divisão dos dois numeros:", a%b)
print("A exponenciação dos dois numeros fica: ", a**b)
print("\nSua idade é:",datetime.datetime.now().year - ano_nascimento)
