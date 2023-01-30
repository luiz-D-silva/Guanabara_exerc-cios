soma = 0
for num in range(6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
print('A soma é {}'.format(soma))
