numeros1 = {2, 4, 6, 8, 10}
numeros2 = {1, 3, 5, 7, 9}
print("A união dos conjuntos 'numeros1' e 'numeros2' é:", numeros1.union(numeros2))
print("A intersecção dos conjuntos 'numeros1' e 'numeros2' é:",numeros1.intersection(numeros2))
print("A diferença do conjunto 'numeros1' em relação ao conjunto 'numeros2' é:", numeros1.difference(numeros2))
print("Os conjuntos 'numeros1' e 'numeros2' são iguais?:", numeros1 == numeros2)
primos = {2, 3, 5, 7}
print("O conjunto 'primos' é um subconjunto do conjunto 'numeros1'?:", primos.issubset(numeros1))