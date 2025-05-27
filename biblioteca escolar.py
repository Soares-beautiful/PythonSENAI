livros = []
while True :
    print('MENU')
    print('')
    print('[1]- Cadastrar livro')
    print('[2]- Exibir livro')
    print('[3]- Mostrar total de livros')
    print('[4]- Lista de títulos')
    print('[5]- Buscar todos os livros de uma determinada categoria')
    print('[6]- Editar dados ')
    print('[7]- Autor que deseja buscar')
    print('[8]- Sair')
    escolha = int(input("faça sua escolha: "))
    
    if escolha == 8:
        print("saindo...")
        break
    elif escolha == 1:
        isbn = int(input("digite o ISBN do seu livro: "))
        titulo = input("digite o titulo do livro: ")
        autor = input("digite o nome do autor: ")
        categoria = input("qual a categoria desse livro: ")
        ano_publicacao = int(input("digite o ano de publicação: "))
        
        livro = {
            "isbn": isbn,
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "ano_de_publicacao": ano_publicacao
        }
        livros.append(livro)
    elif escolha == 2:
        for carro in livros:
            for chave, valor in carro.items():
                print(f"{chave} - {valor}")
            print()
        
    elif escolha == 3:
        quantidade = len(livros)
        print(quantidade)
        
    elif escolha == 4:
        print('lista com titulos')
        for leitura in livros:
            print(f"titulo - {leitura['titulo']}")
            
    elif escolha == 5:
        categoria_busca = input("digite a categoria que deseja")
        print('livros na categoria: ',categoria_busca)
        for leitura in livros:
            if leitura['categoria'] == categoria_busca:
                print(f"titulo - {leitura['titulo']}")
                
    elif escolha == 6:
        isbn_editar = input("digite o novo nome do livro: ")
        for leitura in livros:
            if leitura['isbn'] == isbn_editar:
                nome = input("digite o novo nome do livro")
                autor = input("digite o novo autor")
                categoria = input("digite a nova categoria")
                leitura['nome'] = nome
                leitura['autor'] = autor
                leitura['categoria'] = categoria
                print("dados atualizados")
                break
            else:
                print("livro não encontrado")
                
    elif escolha == 7:
        autor_busca = input("digite o nome do autor que deseja buscar")
        print('Livro do autor:',autor_busca)
        for leitura in livros:
            if leitura['autor'] == autor_busca:
                print(f"titulo - {leitura['titulo']}")
                
    else:
        print("Opção invalida")
