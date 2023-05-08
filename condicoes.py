from random import randint
computador = randint(0, 5)
jogador = int(input('digite um numero'))
print('o seu numero foi: {} \n eu pensei em: {}'.format(jogador,computador))
if jogador == computador:
    print('parabens, você acertou')
else:
    print('você errou')    