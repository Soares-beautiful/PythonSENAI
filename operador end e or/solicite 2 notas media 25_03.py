#solicite 2 notas de um aluno e calcule  a media se a media for maior ou igual 70 aprovado entre 50 e 70 recuperação abaixo de 50 reprovado

nota1 = int(input('solicite uma nota'))
nota2 = int(input('solicite outra nota'))
soma = nota1 + nota2
media = soma/2

if media >=70:
    exibir= 'aprovado'
elif media >=50 and 70:
    exibir= 'de recuperação'
elif media <50:
    exibir= 'reprovado'
print("o aluno esta", exibir)