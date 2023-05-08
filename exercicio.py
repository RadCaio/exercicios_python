print('escolha qual comida você vai querer comer hoje')
print('1) Lagosta')
print('2) Queijo')
print('3) Carne')
menu = str(input('qual comida dessa lista você vai querer comer?'))
if menu == 'Lagosta' or menu == 'lagosta':
    print('ótima escolha')
elif menu == 'Queijo' or menu == 'queijo':
    print('esse é do bom')
elif menu == 'Carne' or menu == 'carne':
    print('já esta saindo no ponto')
else:
    print('não temos essa comida no cardapio')