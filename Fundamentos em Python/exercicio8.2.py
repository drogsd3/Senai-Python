idade = int(input("Digite a sua idade: "))
estudante = input("Você é estudante? Sim/Não: ")
if idade >= 60 or estudante == "Sim":
    print("Desconto de 50% para você")
else:
    print("Sem desconto :(")