import random


while True :
    print("MENU")
    print("")
    print("[2]-Par")
    print("[1]-Impar")
    print("[0]-Sair")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 0:
        print("o usuario saiu")
        break 
    num = int(input("digite um numero de 1 a 10: "))
    maquina = random.randint(0,10)
    soma = num + maquina
    print("a maquina escolheu o numero",maquina)
    print("você escolheu",num)
    print("")
    if escolha == 1 and soma % 2 == 0:
        print(" o resultado é", soma,"Numero par você ganhou")
    elif escolha == 1 and soma % 2 == 1:
        print("o resultado é",soma,"Numero impar você perdeu")
    elif escolha == 2 and soma % 2 == 0:
        print("o resultado é",soma,"Numero par você perdeu")
    elif escolha == 2 and soma % 2 == 1:
        print("o resultado é",soma,"numero impar você ganhou")
        