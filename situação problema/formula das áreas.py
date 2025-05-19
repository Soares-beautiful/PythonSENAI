# triângulo Equilátero
lado = int(input('digite o valor do lado do triangulo: '))
lado2 = lado * lado
raiz = round(3 ** 0.5, 2)
lado3 = lado2 * raiz
area_triangulo = lado3 / 4
print('o valor da area do triangulo é: ', area_triangulo)
#hexagono
area_hexagono = area_triangulo * 6
print(' a area do triangulo é : ', area_hexagono)