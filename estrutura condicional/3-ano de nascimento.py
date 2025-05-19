#solicite o ano de nascimento de uma pessoas e verifique se ela é maior de idade
ano= int(input('digite o ano de nascimento'))
idade = ano - 2025
if idade <18:
    verifica= 'menor de idade'
elif idade >18:
    verifica= 'maior de idade'
print(' voce é',verifica)