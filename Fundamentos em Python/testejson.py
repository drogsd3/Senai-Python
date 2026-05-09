import json

data = {'nome': 'Maria', 'idade': 28}
json_str = json.dumps(data)
print(json_str)

try:
    with open('lista.json', 'r', encoding='utf-8') as arquivo:
        dado = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encotrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON.")

print(dado[0])