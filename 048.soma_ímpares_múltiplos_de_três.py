'''Exercício Python 048: Faça um programa que calcule a soma entre todos os
números que são múltiplos de três e que se encontram no intervalo de 1 até
500.'''

soma = 0
cont = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        cont += 1
        soma += contagem
print('A soma dos {} números é {}'.format(cont, soma))
