sexo = str(input('qual o seu sexo? (M/F )')).strip().upper() [0]
while sexo not in 'MmFf':
    sexo = str(input('dado invalido. digite novamente:')).strip().upper() [0]
print('sexo {} registrado.'.format(sexo))
