saldo_em_conta = float(input('Digite o valor da sua conta:'))
valor_do_saque = float(input('Digite o valor do saque:'))

pode_executar_saque = valor_do_saque <= saldo_em_conta

#print(f'Posso efetuar o saque: {pode_executar_saque}')

if pode_executar_saque:
    print('Você pode sacar')
else:
    print('Você não pode sacar por saldo insuficiente')