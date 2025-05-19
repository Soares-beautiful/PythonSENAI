def input_str(mensagem):
    while True :
        nome = str(input(mensagem))
        if not nome.isalpha():
            print("digite apenas letras")
        else:
            return nome
        
def input_int(mensagem):
    while True :
        try :
            num_int = int(input(mensagem))
            return num_int
        except ValueError:
            print("digite apenas numeros")
            
def input_float(mensagem):
    while True :
        try :
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("digite apenas numeros não inteiros")