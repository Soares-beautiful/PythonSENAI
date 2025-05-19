#solicite dois numeros e verifique qual deles é maior

n1 = int(input('digite um numero'))
n2 = int(input('digite outro numero'))
if n1 > n2:
    verifica= 'primeiro'
elif n1 < n2:
    verifica= 'segundo'

print('o numero maior e o',verifica)
    