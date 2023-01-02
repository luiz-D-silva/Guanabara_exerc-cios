preço = float(input('Qual o preço do produto? R$:'))
# desconto = preço * 5/100
# preço2 = desconto
# newpreço = preço - preço2
newpreço = preço - (preço * 5/100)
print(
    'O valor do produto com desconto de 5% aplicado é: R${:.2f}'.format
    (newpreço))
