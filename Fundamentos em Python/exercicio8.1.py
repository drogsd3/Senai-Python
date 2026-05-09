idade = int(input("Digite sua idade: "))
condicao = input("Faz uso de algum medicamento? Sim/Não: ")
if idade < 18 or condicao == "Sim":
    print("Não pode ingerir bebida alcoolica!")
else:
    print("Pode ingerir bebida alcoolica!")