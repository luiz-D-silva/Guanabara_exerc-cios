nome = str(input('Digite seu nome completo: ')).strip()
n = nome.upper().split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))


'''Solução alternativa de um usuário do Youtube nos comentários

o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim
como [-2] seria a penúltima e assim por diante.

Portanto, podemos resolver da seguinte forma:

nome = input('Qual o seu nome completo? ')
m = nome.split()
print(f'Seu primeiro nome é {m[0]} e seu último nome é {m[-1]}')'''
