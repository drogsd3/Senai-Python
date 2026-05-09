#If or else
idade = int(input("Digite sua idade: "))
if idade <=12 or idade >= 65:
    print("Desconto de 50% no ingresso aplicado.")
else:
    print("Ingreso no valor completo.")

#Condiçoes OR 
cartao = input("\nVocê tem um cartão de acesso? Sim ou Não: ")
permissao = input("Você tem permissão de acesso? Sim ou Não: ")
if cartao == "Sim" or permissao == "Sim":
    print("Acesso liberado.")
else:
    print("Acesso negado.")