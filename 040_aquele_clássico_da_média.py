'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5:
    print('A média é {:.1f}. O aluno foi REPROVADO.'.format(média))
elif 7 > média <= 6.9:
    print('A média é {:.1f}. O aluno está em RECUPERAÇÃO.'.format(média))
else:
    print('A média é {:.1f}. O aluno foi APROVADO.'.format(média))
