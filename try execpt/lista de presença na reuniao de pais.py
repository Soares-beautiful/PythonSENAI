import inputs

lista = []
presentes = []
ausentes = []

def menu_reuniao():
    print('MENU')
    print('')
    print('[1]- Cadastrar nomes dos pais')
    print('[2]- Exibir o total de pais')
    print('[3]- Exibir a lista de nomes em ordem alfabética')
    print('[4]- Realizar confirmação de presença dois pais')
    print('[5]- Exibir um relatório da chamada')

while True :

    menu_reuniao()
        
    escolha = inputs.input_int("faça sua escolha: ")
        
        
    if escolha == 1:
        nome = inputs.input_str("digite o nome de seu responsavel: ")
        if  nome in lista:
            print('Este nome já esta na lista')
        else:
            (lista.append(nome))
            print("nome cadastrado")
    elif   escolha == 2:
        print(len(lista))
            
    elif escolha == 3:
        lista.sort()
        for nome in lista:
            print(nome)
    elif  escolha == 4:
        print('confirme a presença: ')
        for nome in lista:
            print(nome)
            pergunta = inputs.input_str("digite (s/n): ")
            if pergunta == "s":
                presentes.append(nome)
            elif pergunta == "n":
                ausentes.append(nome)
                    
    elif escolha == 5:
        print("Presentes: ")
        for nome in presentes:
            print(nome)
            print("")
        print("Ausentes: ")
        for nome in ausentes:
            print(nome)
            print("")
