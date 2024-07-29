letras = {"a", "e", "i", "o", "u"}
print(f"O conjunto 'letras' tem {len(letras)} elementos.")
letras.add("b")
#print(letras)
if "i" in letras:
    print("Sim, a vogal 'i'está presente no conjunto 'letras'.")
else:
    print("Não, a vogal 'i'não está presente no conjunto 'letras'.")
letras.remove("b")
#print(letras)
consoantes = {"b", "d", "f"}
if consoantes in letras:
    print("Sim, o cojunto 'consoantes' está contido no conjunto 'letras'.")
else:
    print("Não, o cojunto 'consoantes'não está contido no conjunto 'letras'.")
letras.update(consoantes)
print(letras)