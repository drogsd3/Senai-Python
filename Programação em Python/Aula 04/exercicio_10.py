'''10: Desafio Combinado - Cartão de Visita Simples
10.1 Crie uma variável com o nome: nome_completo com o valor
"cleisson morato" (tudo minúsculo, use seu nome).
10.2 Crie uma variável com o nome: cargo com o valor
"DESENVOLVEDOR PYTHON" (tudo maiúsculo).
10.3 Usando F-strings e os métodos de string apropriados *dentro*
da F-string, exiba as seguintes duas linhas:
- Linha 1: O nome formatado como título (Ex: Carlos
Eduardo Souza)
- Linha 2: O cargo formatado em minúsculas (Ex:
desenvolvedor python)
'''
nome_completo = 'douglas mendes'
cargo = 'DESENVOLVEDOR PYTHON'
print(f'{nome_completo.title()} - {cargo.lower()}')