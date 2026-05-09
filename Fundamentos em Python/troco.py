valor = int(input("Digite o valor que você precisa pagar: "))
cedulas = 0

while True:
    if valor >= 100:
        cedulas = valor//100
        print(f"Você precisará de {cedulas} de R$100")
        valor -= cedulas*100
    elif valor >= 50:
        cedulas = valor//50
        print(f"Você precisará de {cedulas} de R$50")
        valor -= cedulas*50
    elif valor >= 20:
        cedulas = valor//20
        print(f"Você precisará de {cedulas} de R$20")
        valor -= cedulas*20
    elif valor >= 10:
        cedulas = valor//10
        print(f"Você precisará de {cedulas} de R$10")
        valor -= cedulas*10
    elif valor >= 5:
        cedulas = valor//5
        print(f"Você precisará de {cedulas} de R$5")
        valor -= cedulas*5
    elif valor >= 1:
        print(f"Você precisará de {valor} de R$1")
        valor -= valor
    else:
        break