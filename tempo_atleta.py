from datetime import date
data_atual = date.today().year
ano_nasc = int(input('qual o seu ano de nascimento?'))
idade = data_atual - ano_nasc
print('o Atleta tem {} anos'.format(idade))
if idade <= 9:
    print('mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('junior')
elif idade <= 20:
    print('sênior')
else:
    print('master')