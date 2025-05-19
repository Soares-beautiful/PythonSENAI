n1= int(input("solicite um numero: "))
n2= int(input("solicite outro numero: "))
n3= int(input("solicite outro numero: "))
if n2> n3 and n1:
    v = 'o primeiro'
if n2> n1 and n3:
    v = 'o segundo'
if n3> n1 and n2:
    v = 'o terceiro'
print('o maior numero é',v)