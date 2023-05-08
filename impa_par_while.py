numero = 1
par = impar = 0
while numero != 0:    
    numero = int(input('digite um numero:'))
    if numero != 0:
        if numero % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('você digitou {} números pares e {} números ímpares'.format(par,impar))