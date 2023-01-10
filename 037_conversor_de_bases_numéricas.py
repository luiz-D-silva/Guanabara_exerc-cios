num = int(input('Escolha um número para conversão:'))
print('''Escolha uma opção para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opçao = int(input('Sua escolha:'))
if opçao == 1:
    print('O número {} em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O número {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('O número {} em HEXAGONAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')
