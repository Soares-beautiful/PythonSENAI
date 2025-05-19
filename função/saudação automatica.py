from datetime import datetime



def saudacao(nome):
    horario = datetime.now().hour
    if horario >=0 and horario <=5:
        print(  "boa madrugada", nome)
    elif horario >=5.1 and horario <=12:
        print(  "bom dia", nome)
    elif horario >=12.1 and horario <=19:
        print(  "boa tarde",nome)
    elif horario >=19.1 and horario <=23.59:
        print(  "boa noite", nome)
    
nome = input("digite seu nome: ")
saudacao(nome)
    
    
    
    
    