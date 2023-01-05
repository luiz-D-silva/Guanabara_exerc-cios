nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('A sua média foi {:.2}'.format(média))
# 1° fórmula de resolução
'''if média >= 6.0:
    print('Sua média foi boa, PARABÉNS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')'''
# 2° fórmula de resolução
print('PARABÉNS!' if média >= 6.0 else 'ESTUDE MAIS!')
