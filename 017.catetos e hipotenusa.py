from math import hypot

'''Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.'''

# solução 1

'''cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
# (1/2) calcula a raiz quadrada
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

# solução 2

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa vai medir {:.2}'.format(hip))
