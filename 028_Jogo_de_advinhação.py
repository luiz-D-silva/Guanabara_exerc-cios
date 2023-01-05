'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou
perdeu.'''

from random import randint
from time import sleep  # faz o computador esperar para mostrar a resposta

computador = randint(0, 5)  # faz o computador "pensar"/sortear
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)  # vai aguardar 2 segundos antes de printar a resposta
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errou, pensei em {} e não em {}, mais sorte na próxima vez!'.
          format(computador, jogador))
