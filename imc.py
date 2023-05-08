peso = float(input('digite o seu peso:'))
altura = float(input('digite a sua altura'))
imc = peso / (altura * altura)
print('o seu IMC é de: {:.2f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and  imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')