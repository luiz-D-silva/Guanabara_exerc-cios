# meu código, resolução 1
nome = (input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculo é: ', (nome.upper()))
print('Seu nome em minúsculo é: ', (nome.lower()))
print('Seu nome tem ao todo', len(nome.strip()), 'letras')
print('Seu primeiro nome é', (nome.split()[
      0]), 'e ele tem', (len(nome.split()[0])), 'letras')
print('Seu segundo nome é', (nome.split()[
      1]), 'e ele tem', (len(nome.split()[1])), 'letras')
print('Seu terceiro nome é', (nome.split()[
      2]), 'e ele tem', (len(nome.split()[2])))


'''# com o código Guanabara, resolução 2
nome = str(input('Digite seu nome completo: ')).strip()
# strip elimina os espaços antes e depois do nome, os centrais permanecem
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# len conta os caracteres de nome subtraído dos espaços em branco
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# find encontra o primeiro espaço na palavra e imprime sua numeração, o que vai
# coincidir com a quantidade de letras do primeiro nome.

# outra forma, segue abaixo
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(
    separa[0], len(separa[0])))


# código de um comentário do vídeo, resolução 3
nome = str(input('Digite o seu nome completo!: '))

espaço = nome.strip()
maiúsculo = nome.upper()
minúsculo = nome.lower()
letras = len(nome) - nome.count(' ')
primeiro = nome.find(' ')

print(f'Seu nome em letras maiúsculas: {maiúsculo}!')

print(f'Seu nome em letras minúsculas: {minúsculo}!')

print(f'Seu nome tem {letras} letras!')

print(f'Seu primeiro nome tem {primeiro} letras!')'''
