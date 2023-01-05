# o programa identifica a palavra silva dentro de uma string
nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
