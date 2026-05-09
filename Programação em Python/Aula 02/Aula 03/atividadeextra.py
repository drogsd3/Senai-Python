#Exericio 01 
while True:
    try:
        ano = int(input("Digite quantos anos o veiculo tem: "))
        if ano > 5:
            print("Esse veiculo precisa de manutenção")
            break
        elif ano < 0:
            print("\nDigite um numero positivo")
        else:
            print(f"\nO veiculo não precisa de manutenção!\nFalta {5 - ano} anos para fazer a proxima manutenção!")
            break
    except ValueError:
        print("\nXX ENTRADA INVÁLIDA! XX\nDigite um numero valido")

#Exercicio 02
valor = float(input("Digite um salário: "))

if valor > 1200.00:
    print("Com esse salário será necessário pagar imposto.")
else:
    print("Com esse salário NÃO será necessário pagar imposto.")

#Exercicio 03
metro = float(input("Digite uma medida em metro: "))
milimetro = metro * 1000

print(f"{metro}M é equivalente a {milimetro:.2f}ML")

#Exercicio 04
numero = float(input("Digite um numero: "))
if numero > 0:
    print("Esse numero é positivo.")
elif numero < 0:
    print("Esse numero é negativo")
else:
    print("Esse numero é ZERO 😁")

#Exercicio 05
numero =  float(input("Digite um numero: "))
if numero % 2 > 0:
    print("Esse numero é impar")
else:
    print("Esse numero é par")