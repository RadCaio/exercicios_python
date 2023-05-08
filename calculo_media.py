nota1 = float(input('digite a sua primeira nota:'))
nota2 = float(input('digite a sua segunda nota:'))
media = (nota1 + nota2) / 2
print('sua nota foi: {}'.format(media))
if media >= 7:
    print('parabéns, você passou!')
elif media >= 5 and media < 7:
    print('você ficou em recuperação, estude mais.')
elif media < 5:
    print('você foi reprovado')        