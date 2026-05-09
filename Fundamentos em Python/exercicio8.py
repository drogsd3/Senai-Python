ticket = input("Você tem o ingresso para essa viagem? Sim/Não: ")
documento = input("Ou documento para verificar no sistema? Sim/Não: ")
if ticket == "Sim" or documento == "Sim":
    print("Acesso permitido")
else:
    print("Acesso negado")