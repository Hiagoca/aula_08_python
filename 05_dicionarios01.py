agenda = {}
agenda["Pedro"] = {
    "telefone": "987654321",
    "email": "pedro@gmail.com"
}
agenda["Maria"] = {
    "telefone": "12345678",
    "email": "maria@hotmail.com"
}
agenda["Ana"] = {
    "telefone": "963258741",
    "email": "ana@yahoo.com.br"

}

primeiro_amigo = list(agenda.keys())[0]
print(f"O Telefone do {primeiro_amigo}, primeiro amigo da agenda é:",agenda[primeiro_amigo]["telefone"])

agenda["Maria"]["email"] = "maria@outlook.com"
agenda["Ana"]["Cidade"] = "Campinas"

#Informações do terceiro amigo de uma forma mais simplificada.
print(agenda["Ana"])

#Informações do terceiro amigo de uma forma mais completa e organizada.
print("Informções da Ana:")
for chaves, valor in agenda["Ana"].items():
    print(f"{chaves}: {valor}")



