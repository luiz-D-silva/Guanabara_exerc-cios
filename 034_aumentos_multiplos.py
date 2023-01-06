'''Escreva um programa que pergunte o salário de um funcionário e calcule o
valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento
de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salário = float(input('Qual é o seu salário? '))
aumento = salário * 15/100
aumento2 = salário * 10/100
if salário <= 1250:
    print(
        f'Com aumento de 10%, o salário passa a ser R${salário+aumento2:.2f}')
else:
    print(
        f'Com aumento de 15%, o salário passa a ser R${salário+aumento:.2f}')


# resolução do  Guanabara
'''salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário + 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(
    salário, novo))'''
