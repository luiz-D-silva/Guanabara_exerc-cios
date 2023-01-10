from datetime import date

anoatual = date.today().year
nascimento = int(input('Digite sua data de nascimento: '))
idade = anoatual - nascimento
print('Quem nasceu em {}, tem {} anos de idade em {}'.
      format(nascimento, idade, anoatual))
if idade == 18:
    print('{} É o ano do seu alistamento!'.format(anoatual))
elif idade < 18:
    print('Falta(m) {} ano(s) para seu alistamento'.
          format(18-idade))
elif idade > 18:
    print('Deveria ter se alistado há {} anos'.
          format(idade-18))
