#crie um programa que leia o peso e a altura de uma pessoa e calcule seu IMC

peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
imc = peso/ (altura * altura)

if imc >=0 and imc <=18.5:
    exibir= "magreza"
elif imc >= 18.5 and imc <=24.9:
    exibir= "normal"
elif imc >= 25.0 and imc <=29.9:
    exibir= "sobrepeso"
elif imc >= 30.0 and imc <=34.9:
    exibir= "obesidade de grau 1"
elif imc >=35.0 and imc <=39.9:
    exibir= "obesidade de grau 2"
elif imc >40:
    exibir= "obesidade de grau 3"
print("o IMC do usuario é",exibir)
