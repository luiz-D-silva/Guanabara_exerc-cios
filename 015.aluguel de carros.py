# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
# pagar, sabendo que o carro custa R$60 por dia e R$0, 15 por Km rodado.

km_percorridos = float(input('Qual a quantidade de quilômetros percorrida? '))
dias = int(input('Qual a quantidade de diária(s)? '))
preço_por_km_rodado = km_percorridos * 0.15
preço_por_dia = dias * 60
aluguel = preço_por_dia + preço_por_km_rodado

print('O valor do alguel para {} dias e {} km é R${:.2f}'.format(

    dias, km_percorridos, aluguel))

# código do guanabara
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
# fim do código

# o que eu prometo é luta, não prometo sucesso!
