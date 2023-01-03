# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento.

salário = float(input('Qual o salário do funcionário? '))
novo_salário = salário + (salário * (15/100))
print(
    'Baseado no salário R${:.2f}, o novo salário, acrescido 15% é R${:.2f}'.
    format(salário, novo_salário))
