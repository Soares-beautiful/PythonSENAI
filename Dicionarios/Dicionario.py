
#------Dicionarios-----

#Criar
aluno = {
    "nome":"João Pedro",
    "idade": 2,
    "altura": 1.76,
    "matriculado": True 
}

carro = {
    "nome":"Gol bolinha",
    "ano_de_fabricacao": 1994,
    "cor": "Vermelho"
}

carro2 = {
    "nome":"Citroen Picasso",
    "ano_de_fabricacao": 1999,
    "cor": "Azul"
}

carro3 = {
    "nome": "chevrolet zafira",
    "ano_de_fabricacao": 2001,
    "cor": "Cinza"
}
#print(aluno)

#Adicionar campo
aluno["peso"] = 65

#print(aluno)
#Alterar campo
aluno["idade"] = 3

#print(aluno)

#Deletar campo
del aluno["altura"]

#print(aluno)

# Verificar
if "altura" in aluno:
    print("Altura existente")
else:
    print("Altura inexistente")

# Exibir
for chave, valor in aluno.items():
    print(f"{chave} = {valor}")
    
#Exibir uma lista de Dicionarios
lista_carros = [carro, carro2, carro3]

    # Escolhendo os campos
for carro in lista_carros:
    print(f"{carro['ano_de_fabricacao']}")
    #Exibindo todos
for carro in lista_carros:
    for chave, valor in carro.items():
        print(f"{chave} - {valor}")
    print()