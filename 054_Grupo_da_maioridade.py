'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''

from datetime import date

anoatual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoas)))
    idade = anoatual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('='*50)
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
