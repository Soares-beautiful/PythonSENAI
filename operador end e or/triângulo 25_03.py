#desenvolva um programa que leia os 3 lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno

lado1 = input("digite o primeiro lado")
lado2 = input("digite o segundo lado")
lado3 = input("digite o terceiro lado")

if lado1 == lado2 and lado1 == lado3 and lado3 == lado2:
    exibir = " equilatero"
elif lado1 == lado2 or lado2 == lado3 and lado2!= lado2 or lado2 != lado1:
    exibir = " isóceles"
elif lado1 !=lado2 and lado1 != lado2 and lado1 != lado2:
    exibir = " escaleno"
print("o triângulo é",exibir)