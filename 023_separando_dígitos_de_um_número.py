num = int(input('Digite um número de até 4 dígitos? '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Undidade = {}'.format(u))
print('Dezena = {}'.format(d))
print('Centena = {}'.format(c))
print('Milhar = {}'.format(m))
