frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase {} \033[32mÉ UM PALÍNDROMO!.'.format(frase))
else:
    print('A frase digitada não é um palíndromo')
