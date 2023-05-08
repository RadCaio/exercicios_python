nome = str(input('qual o seu nome?'))
if nome == 'Caio':
    print('você tem um nome de um Deus')
elif nome == 'Gabriel' or nome == 'Julia' or nome == 'Igor':
    print('seu nome é muito básico.')
else:
    print('nunca ouvi o seu nome.')
print('tenha uma boa semana, {}!'.format(nome))    