import random
pc = random.randint(0, 100)  
   

print("")
print("BEM-VINDO AO JOGO")
print("")
print("Adivinhe o numero de 1 a 100: ")
print("")


   
while True:
    palpite = int(input("Digite seu palpite"))  
    if palpite > pc:
        print('O número é menor que', palpite)
    elif palpite < pc:
        print('O número é maior que', palpite)
    elif palpite == pc:
        print('Você acertou!')
        print('1 - Para sair')
        print('2 - Para continuar')
        continuar = int(input('Digite sua escolha '))  
           
        if continuar == 2:
            print("Quer jogar denovo meu truta?")
            pc = random.randint(0, 100)
           
               
        else:
            print("O usuario saiu...")
            break  