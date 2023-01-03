'''Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
# os valores de seno, cosseno e tangente saõ dados em radianos
# por isso necessita-se usr a função 'math.radians' para converter de
# radianos para graus centrígrados
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Para o ângulo de {}°'.format(angulo))
print(' Temos:\n O SENO de {:.2}\n O COSSENO de {:.2}\n A TANGENTE de {:.2}'.
      format(seno, cosseno, tangente))
