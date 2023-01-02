# Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

c = float(input('Qual a temperatura em graus C°? '))
# anteriormente feito da seguinte forma "f = ((9*c) / 5) + 32"
# observar que seguindo a ordem de precedência, dispensa-se o uso de parênteses
# em caso de dúvidas:https://youtu.be/9l_Gay8BuAw , aos 4:00 minutos da aula
f = 9*c / 5 + 32
print('A temperatura de {0}C° equivale a {1}F°'.format(c, f))
# {0} e {1} indicam a ordem, se trocados exibem o conforme a reorganização
