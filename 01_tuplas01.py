minha_tupla = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta")
print(minha_tupla[3])
x = list(minha_tupla)
x[4] = "preto"
minha_tupla = tuple(x)
print(minha_tupla)
cores_invertidas = minha_tupla[::-1]
print(cores_invertidas)


