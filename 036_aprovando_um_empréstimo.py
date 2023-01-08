'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. Pergunte o casa da casa, o salário do comprador e em quantos anos ele
vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.'''

casa = float(input('Qual o casa da casa? R$'))
salário = float(input('Qual o casa do salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos*12)
mínimo = salário*30/100
if prestação <= mínimo:
    print("""Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}
    Empréstimo pode ser CONCEDIDO!""".format(casa, anos, prestação))
else:
    print("""A prestação de R${:.2f}, excede o valor de R${:.2f}
    Equivalente aos 30% Da sua renda salarial.
    O empréstimo foi NEGADO! """.format(prestação, mínimo))
