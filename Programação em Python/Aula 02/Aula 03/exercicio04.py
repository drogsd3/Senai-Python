n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
soma = n1 + n2
dividir = soma/n3
print(f"""
---- RESULTADO ----
A soma de {n1} e {n2} é: {soma}
A divisão de {soma} por {n3} é: {dividir:.2f}
-------------------------------""")