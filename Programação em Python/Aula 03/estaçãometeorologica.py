cidade = input("Digite o nome da sua cidade: ")
temperatura = input("Digite a temperatura (em °C): ")
umidade = input("Digite a umidade do ar (em %): ")
condicao = input("Digite a condição do tempo (ex: ensolarado, nublado, chuvoso): ")

print(f"""
------- Previsão do Tempo --------
Cidade: {cidade}
Temperatura: {temperatura}°C
Umidade: {umidade}%
Condição: {condicao}
--------------------------------""")