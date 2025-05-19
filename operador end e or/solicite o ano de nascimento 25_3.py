#solicite o ano de nascimento de uma pessoa, calcule a idade e verifique a faixa etaria da pessoa ( abaixo de 10 é criança, de 11 a 17 adolecente, de 18 a 59 adulto, acima de 60 idoso

nascimento = int(input("digite seu ano de nascimento"))
ano_atual = 2025
idade = ano_atual - nascimento

if idade >0 and idade <=10:
    exibir= " é criança"
elif idade >10 and idade <=17:
    exibir= " é adolescente"
elif idade >=18 and idade <=59:
    exibir= " é adulto"
elif idade >=60 and idade <115:
    exibir= " é idoso"
else:
    exibir = "idade invalida"
print(exibir)

    
