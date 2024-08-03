def calcula_media(notas):
    total = sum(notas.values())
    quantidade = len(notas)
    media = total / quantidade
    return media

alunos = {
    "Joao":{
        "matematica": 7.9,
        "portugues": 8.4,
        "historia": 9.3
    },
    "Marcia": {
        "matematica": 9.0,
        "portugues": 8.7,
        "historia": 8.5    
    },
    "Ana": {
        "matematica": 9.3,
        "portugues": 7.8,
        "historia": 8.4
    }
}

for aluno, notas in alunos.items():
    media = calcula_media(notas)
    print(f"{aluno}: {media:.2f}")