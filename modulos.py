import random
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
lista = [a1,a2,a3,a4]
escolhido = random.shuffle(lista)
print('a ordem de apresentação será:')
print(lista)