import inputs

lista = []

while True :
    print('MENU')
    print('')
    print('[1]- Cadastra nomes')
    print('[2]- Exibir o total de inscritos')
    print('[3]- Exibir a lista de nomes em ordem alfabética')
    print('[4]- Permitir a consulta de um nome')
    
    escolha = inputs.input_int("faça sua escolha")
    
    
    if escolha == 1:
        nome = inputs.input_str('Digite seu nome: ')
        if nome in lista:
            print('Este nome já esta na lista')
        else:
            lista.append(nome)
            print("nome cadastrado")
    elif escolha == 2:
        print(len(lista))
        
    elif escolha == 3:
        lista.sort()
        for nome in lista:
            print(nome)
    elif escolha == 4:
        nome = inputs.input_str("digite seu nome")
        if nome in lista:
            print("nome encontrado deseja remove-lo (s/n)")
            resposta = inputs.input_str('faça sua escolha')
            if resposta == 's':
                lista.remove(nome)
                print("nome removido")
        else:
            print("nome não encontrado")
            adicionar = inputs.input_str("deseja adicionar um nome a lista (s/n)")
            if adicionar == 's':
                lista.append(nome)
                print("nome adicionado")