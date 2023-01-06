'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 parta viagens mais longas.'''

'''distância = float(
    input('Quantos quilômetros de distância serão percorridos? '))
if distância <= 200:
    print('O valor do seu bilhete a R$0.50 Km é R${:.2f}'.
          format(distância * 0.50))
else:
    print('O valor do seu bilhete a R$0,45 Km é R${:.2f}'.
          format(distância * 0.45))
'''

# ou

'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

# ou usando o format simplificado

distancia = float(input('Qual a distância da viagem em Km? '))
if distancia <= 200:
    print(f'O valor da passagem é R${distancia*0.5:.2f}')
else:
    print(f'O valor da passagem é R${distancia*0.45:.2f}')
