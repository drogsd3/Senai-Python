#Revisão e Introdução ao input
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

print(f"""
------------------------
Cadastro de usuário:
Nome: {nome} {type(nome)}
Idade: {idade} anos {type(idade)}
Cidade: {cidade} {type(cidade)}
-------------------------""")
