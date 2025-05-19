#solicite um numero ao usuario e verifique se ele é positivo ou negativo

numero = int(input("solicite um numero: "))
if numero < 0 :
    verifica:'negativo'
    print('o numero', verifica)
elif numero > 0 :
    verifica = 'positivo'
print('o numero é',verifica)