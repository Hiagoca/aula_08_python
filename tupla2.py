frutas = ("banana", "maçã", "laranja")
legumes = ("tomate", "cenoura", "batata")
mercado = frutas + legumes
print(mercado)
if "banana" in mercado:
    print("Sim, banana está presente na tupla mercado")
if "alface" in mercado:
    print("Sim, alface está presente na tupla mercado")
else:
    print("Não, alface não está presente na tupla mercado")
print(mercado[-1])