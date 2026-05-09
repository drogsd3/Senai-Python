import time
fila = []

def menu():
    print("""
    1 - Adicione uma nova pessoa.
    2 - Atender pessoa.
    3 - Exibir a fila atual.
    4 - Exibir a fila de espera.
    5 - Sair do programa\n      
    """)

while True:
    menu()
    opcao = input('Digite a opção: ')

    if opcao == '1':
        fila.append(input("Digite o nome dessa pessoa: "))        
    elif opcao == "2":
        if len(fila)>0:
            atendido = fila.pop(0)
            print(f"O {atendido} será atendido")
        else:
            print("Não há cliente na fila")
            time.sleep(2)
    elif opcao == "3":
        print(f"A proxima pessoa da fila é: {fila[0]}")
        time.sleep(3)
    elif opcao == "4":
        print(f"Existem {len(fila)} em espera")
        print(fila)
        time.sleep(5)
    elif opcao == "5":
        print("Tchau")
        break
    else:
        print("Digite uma opção válida.")