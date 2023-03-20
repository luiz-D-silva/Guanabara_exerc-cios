km = float(input('Qual a distância da viagem em Km: '))
if km <= 200:
    print(f'O valor da passagem é R${km*0.50:.2f}')
else:
    print(f'O valor da passagem é R${km*0.45:.2f}')
