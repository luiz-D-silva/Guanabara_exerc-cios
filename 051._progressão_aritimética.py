primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10) * razão
for c in range(primeiro, décimo, razão):
    print('{}'.format(c), end=' → ')
print('Finish')
