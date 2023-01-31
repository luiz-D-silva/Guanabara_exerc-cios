from random import choice
from time import sleep

n1 = str(input('Aluno 1: ')).strip().upper()
n2 = str(input('Aluno 2: ')).strip().upper()
n3 = str(input('Aluno 3: ')).strip().upper()
n4 = str(input('Aluno 4: ')).strip().upper()
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print(' O aluno sorteado foi:')
sleep(2)
print('.')
sleep(0.5)
print('..')
sleep(1)
print('...')
sleep(1.5)
print('....{}'.format(sorteado))
