''' Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo.'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
if n1 < (n2+n3) and n2 < (n1+n3) and n3 < (n1+n2):
    print('Os valores {:.2f}, {:.2f} e {:.2f} PODEM formar um triângulo'.
          format(n1, n2, n3))
else:
    print('Os valores {:.2f}, {:.2f} e {:.2f} NÃO PODEM formar um triângulo'.
          format(n1, n2, n3))
