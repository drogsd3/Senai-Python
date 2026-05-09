velocidade = int(input("Digite a velocidade do veiculo: "))
if velocidade >=100:
    print("Multa gravissima")
elif velocidade >=80:
    print("Multa grave")
elif velocidade >=70:
    print("Multa")
else:
    print("Velocidade normal")