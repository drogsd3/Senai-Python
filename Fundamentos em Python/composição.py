idade = 27
nome = "Douglas"
dinheiro = 51.60
print("Apresentação no formato normal %f" %dinheiro) #para numeros flutuantes é padrão 8 digitos
print("Para mostra menos numeros após a virgula %4.2f" %dinheiro)
print("Mostra numero com mais zero %03d" %idade)
print("Apresentar o dinheiro com formato de moeda brasileira R$%5.2f" %dinheiro)

#Composição usando o metodo format
print("\nApresentação no formato normal {}".format(dinheiro)) #O format ignora o zero
print("Apresentar formato em moeda com o format {:5.2f}".format(dinheiro))