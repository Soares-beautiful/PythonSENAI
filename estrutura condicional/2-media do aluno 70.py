nota = int(input('solicite uma nota'))
nota2 = int(input('solicite outra nota'))
soma = nota + nota2
media = soma / 2
if media < 70 :
    verifica = 'reprovado'
elif media > 70 :
    verifica = 'aprovado'
print('o aluno esta',verifica)
