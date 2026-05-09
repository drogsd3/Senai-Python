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

    
    