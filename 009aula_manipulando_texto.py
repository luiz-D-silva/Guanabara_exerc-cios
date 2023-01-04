'''As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(),
 lower(), capitalize(), title(), strip(), junção com join().'''

# exercício aos 00:30 m de aula

frase = 'Curso em Vídeo Python   '
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))  # conta o 'o' minúsculo

print(frase.count('O'))  # conta o 'O' maiúsculo

print(frase.upper().count('O'))
# upper deixa os 'O's maiúsculos e
# que juntamente com o comando 'cout' confere
# todos os 'O's, pois agora todos são maiúsculos

print(len(frase))  # confere o tamanho da frase, incluindo espaços

print(len(frase.strip()))  # remove os espeços indesejados
# confere só os caracteres

print(frase.replace('Python', 'Android'))
# o comando 'replace' faz a troca de nomes
# para salvar o resultado da subistituição, usa-se esse código:
# frase = frase.replace('Python', 'Android')

print('Curso' in frase)  # identifica palavras dentro da frase
print(frase.find('em'))  # identifica a posição em que inicia a palavra

print(frase.lower().find('vídeo'))
# lower transforma em minúsculo #ver linha 18

print(frase.split())
dividido = frase.split()
print(dividido[0])  # mostra apenas a posiçao '0' da nova variável
'''Na linha 40 percebemos que uma nova variável foi criada e que ela usa a
a string inicial para se moldar, formando com os dados daquela instring uma
lista, e a nova variável recebeu essa lista como valor'''

print(dividido[2][3])
# mostra a letra de posição 3, dentro da palavra 2

# utilizando print de três aspas para textos longos#

'''print("""Elas [as pessoas grandes] adoram os números. Quando a gente lhes
fala de um novo amigo, as pessoas grandes jamais se interessam em saber como
ele realmente é. […] Mas perguntam: Qual é a sua idade? Quantos irmãos ele tem?
Quanto pesa? Quanto ganha seu pai?
Somente assim é que elas julgam conhecê-lo

By: O pequeno Príncipe""")
'''
